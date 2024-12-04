#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from collections import deque
import paho.mqtt.client as mqtt # install paho-mqtt thru pip if not on the system alr
import os

# MISC
TURTLEBOT_ID = int(os.environ['PI_ID']) # will be 2-7
global ros_pub
global mqtt_client
available = True

# MQTT Configuration
MQTT_BROKER = rospy.get_param('broker_ip', "192.168.0.41")        # Desktop (master) IP
MQTT_PORT = int(rospy.get_param('port', 1883))                    # Port
MQTT_TOPIC_SUB = "pi/deploy"                     # MQTT topic to listen for deployment
MQTT_TOPIC_PUB_0 = "pi/done"                     # MQTT topic to say a pi is done
MQTT_TOPIC_PUB_1 = "pi/unavailable"              # MQTT topic to say a pi is unavailable

# ROS Configuration
ROS_TOPIC_SUB = f"/pi{TURTLEBOT_ID}/status"      # ROS topic to receive status updates from driving, dancing, and greeting
ROS_TOPIC_PUB = f"/pi{TURTLEBOT_ID}/cmd_move"    # ROS topic to publish movement commands

def on_connect(client, userdata, flags, rc):
    """Callback when MQTT connects to the broker."""
    global mqtt_client
    if rc == 0:
        rospy.loginfo("Connected to MQTT Broker!")
        mqtt_client.subscribe(MQTT_TOPIC_SUB)
    else:
        rospy.logerr("Failed to connect to MQTT, return code %d", rc)

def on_message(client, userdata, msg):
    """Callback when a message is received from MQTT."""
    global ros_pub, mqtt_client
    rospy.loginfo("MQTT Message Received: %s -> %s", msg.topic, msg.payload.decode())
    topic, msg = msg.topic, msg.payload.decode()
    print('what')
    try:
        if int(msg) == TURTLEBOT_ID:
            if available and topic == "pi/deploy":
                ros_pub.publish(msg)    # this should call the move file by sending a msg over /pi{ID}/cmd_move, need another script to execute said commands or maybe have them in here?
                rospy.loginfo("Deploying Turtlebot %s", str(TURTLEBOT_ID))
            elif not available:
                mqtt_client.publish(MQTT_TOPIC_PUB_1, str(TURTLEBOT_ID), qos=0)
                rospy.logwarn("Turtlebot requested is unavailable.")
    except Exception as e:
        rospy.loginfo(f"[ERROR] {e}")
    
def ros_callback(data):
    """Callback when a message is received on the ROS topic."""
    rospy.loginfo("ROS Message Received: %s", data.data)
    # Publish the ROS message to the MQTT topic
    print(data.data)
    mqtt_client.publish(data.data, str(TURTLEBOT_ID))
    # need to look into this on how to signal that the turtlebot is done doing its thing
    # if we done....
    # client.publish("pi/done", str(TURTLEBOT_ID))

if __name__ == "__main__":
    # ROS Client
    rospy.init_node(f'ros_pi{TURTLEBOT_ID}_comms', anonymous=True)
    ros_pub = rospy.Publisher(ROS_TOPIC_PUB, String, queue_size=10)
    ros_sub = rospy.Subscriber(ROS_TOPIC_SUB, String, ros_callback)

    # MQTT Cilent
    mqtt_client = mqtt.Client()
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    try:
        mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
    except Exception as e:
        rospy.logerr("Failed to connect to MQTT broker: %s", str(e))

    # Loop MQTT and ROS
    rate = rospy.Rate(1)
    try:
        rospy.loginfo("Loop starting...")
        mqtt_client.loop_start()
        rospy.spin()
    except rospy.ROSInterruptException:
        print("\ninterrupted babyyyyy")
    finally:
        mqtt_client.loop_stop()
        mqtt_client.disconnect()# this should call the move file