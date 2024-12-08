#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import paho.mqtt.client as mqtt # install paho-mqtt thru pip if not on the system alr
import os, time
from turtlebot_saphari import chester

# MISC
TURTLEBOT_ID = int(os.environ['PI_ID']) # will be 2-7
global mqtt_client, available

# MQTT Configuration
MQTT_BROKER = rospy.get_param('broker_ip', "192.168.0.41")        # Desktop (master) IP
MQTT_PORT = int(rospy.get_param('port', 1883))                    # Port
MQTT_TOPIC_SUB = "pi/deploy"                     # MQTT topic to listen for deployment
MQTT_TOPIC_PUB_0 = "pi/done"                     # MQTT topic to say a pi is done
MQTT_TOPIC_PUB_1 = "pi/unavailable"              # MQTT topic to say a pi is unavailable
MQTT_TOPIC_PUB_2 = "pi/pong"                     # MQTT topic to say a pi is ready to receive

def on_connect(client, userdata, flags, rc):
    """Callback when MQTT connects to the broker."""
    global mqtt_client
    if rc == 0:
        rospy.loginfo(f"Connected to MQTT Broker! Turtlebot ID: {TURTLEBOT_ID}")
        mqtt_client.subscribe(MQTT_TOPIC_SUB)
        mqtt_client.subscribe("pi/ping") # yeah idc
    else:
        rospy.logerr("Failed to connect to MQTT, return code %d", rc)

def on_message(client, userdata, msg):
    """Callback when a message is received from MQTT."""
    global mqtt_client, available
    topic, msg = msg.topic, msg.payload.decode()
    if int(msg) != TURTLEBOT_ID:
        return
    rospy.loginfo("MQTT Message Received: %s -> %s", topic, msg)
    try:
        if available and topic == "pi/deploy":
            # DEPLOYYYYY
            available = False
            rospy.loginfo("Deploying Turtlebot %s", str(TURTLEBOT_ID))
            if chester() == 0:
                rospy.loginfo("Movement success! We chilling and done.")
            mqtt_client.publish(MQTT_TOPIC_PUB_0, str(TURTLEBOT_ID), qos=1)
            available = True
        elif not available:
            mqtt_client.publish(MQTT_TOPIC_PUB_1, str(TURTLEBOT_ID), qos=1)
            rospy.logwarn("Turtlebot requested is unavailable.")
        if available and topic == "pi/ping":
            mqtt_client.publish(MQTT_TOPIC_PUB_2, str(TURTLEBOT_ID), qos=1)
    except Exception as e:
        rospy.loginfo(f"[ERROR] {e}")

if __name__ == "__main__":
    # ROS Client
    rospy.init_node(f'turtlebot_mqtt', anonymous=True)

    # MQTT Cilent
    mqtt_client = mqtt.Client()
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    try:
        mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
    except Exception as e:
        rospy.logerr("Failed to connect to MQTT broker: %s", str(e))

    # huh
    available = True

    # Loop MQTT
    try:
        mqtt_client.loop_start()
        while not rospy.is_shutdown():
            rospy.spin()        # need to test this if it fixes sigkill problem
    except Exception as e:
        rospy.logwarn(f'Exception encountered: {e}')
    finally:
        mqtt_client.loop_stop()
        mqtt_client.disconnect()