#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import paho.mqtt.client as mqtt # install paho-mqtt thru pip if not on the system alr
import os

# MQTT Configuration
MQTT_BROKER = rospy.get_param('broker_ip', "192.168.1.41")        # Desktop (master) IP
MQTT_PORT = int(rospy.get_param('port', 1883))                    # Port
MQTT_TOPIC_SUB_ESP = "robot/control"  # MQTT topic to listen for commands
MQTT_TOPIC_PUB_ESP = "robot/status"   # MQTT topic to publish robot status

# ROS Configuration
ROS_TOPIC_SUB = "/cmd_move"        # ROS topic for incoming movement commands
ROS_TOPIC_PUB = "/robot_status"    # ROS topic to publish status updates

# what
TURTLEBOT_ID = os.environ['ROS_IP'] # i forgot the environ name, will get this later lol

def on_connect(client, userdata, flags, rc):
    """Callback when MQTT connects to the broker."""
    if rc == 0:
        rospy.loginfo("Connected to MQTT Broker!")
        
        client.subscribe(MQTT_TOPIC_SUB_ESP)
    else:
        rospy.logerr("Failed to connect to MQTT, return code %d", rc)

def on_message(client, userdata, msg):
    """Callback when a message is received from MQTT."""
    rospy.loginfo("MQTT Message Received: %s -> %s", msg.topic, msg.payload.decode())
    # Publish the MQTT message to a ROS topic
    ros_pub.publish(msg.payload.decode())

def ros_callback(data):
    """Callback when a message is received on the ROS topic."""
    rospy.loginfo("ROS Message Received: %s", data.data)
    # Publish the ROS message to the MQTT topic
    mqtt_client.publish(MQTT_TOPIC_PUB_ESP, data.data)

if __name__ == "__main__":
    # Initialize ROS node
    rospy.init_node('ros_mqtt_bridge', anonymous=True)

    # ROS Subscribers and Publishers
    ros_pub = rospy.Publisher(ROS_TOPIC_PUB, String, queue_size=10)
    ros_sub = rospy.Subscriber(ROS_TOPIC_SUB, String, ros_callback)

    # Initialize MQTT Client
    mqtt_client = mqtt.Client()
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message

    # Connect to MQTT Broker
    try:
        mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
    except Exception as e:
        rospy.logerr("Failed to connect to MQTT broker: %s", str(e))

    # Start MQTT Loop in a separate thread
    mqtt_client.loop_start()

    # ROS Spin Loop
    try:
        rospy.spin()
    except rospy.ROSInterruptException:
        print("interrupted babyyyyy")
        pass
    finally:
        mqtt_client.loop_stop()
        mqtt_client = mqtt.Client()
        mqtt_client.disconnect()