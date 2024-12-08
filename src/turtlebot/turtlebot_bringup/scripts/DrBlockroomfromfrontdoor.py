#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist, PoseStamped
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib

def increase_speed():
    # Adjust the speed dynamically using cmd_vel
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.sleep(1)  # Allow time for the publisher to connect

    move_cmd = Twist()
    
    # Set a higher linear velocity
    move_cmd.linear.x = 1.0  # Forward speed (increase this value for faster movement)
    move_cmd.angular.z = 0.0  # No rotation (straight line)

    rospy.loginfo("Increasing speed and moving robot...")
    
    pub.publish(move_cmd)

def send_goal():
    rospy.init_node('send_goal')

    pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
    rospy.sleep(1)  # Allow time for the node to initialize

    goal = PoseStamped()

    # Set header information
    goal.header.frame_id = "map"
    goal.header.stamp = rospy.Time.now()

    # Set goal position (example values)
    goal.pose.position.x = -10.463
    goal.pose.position.y = -8.523
    goal.pose.position.z = 0.000

    # Set goal orientation (example quaternion)
    goal.pose.orientation.x = 0.0
    goal.pose.orientation.y = 0.0
    goal.pose.orientation.z = -0.752
    goal.pose.orientation.w = 0.659

    pub.publish(goal)
    rospy.loginfo("Goal sent to TurtleBot!")

if __name__ == '__main__':
    try:
        send_goal()
    except rospy.ROSInterruptException:
        pass
