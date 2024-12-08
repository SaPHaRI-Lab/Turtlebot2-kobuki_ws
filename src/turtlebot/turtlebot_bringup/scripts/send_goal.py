#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseStamped

def send_goal():
    rospy.init_node('send_goal')

    pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
    rospy.sleep(1)  # Allow time for the node to initialize

    goal = PoseStamped()

    # Set header information
    goal.header.frame_id = "map"
    goal.header.stamp = rospy.Time.now()

    # Set goal position (example values)
    goal.pose.position.x = -6.087
    goal.pose.position.y = -7.811
    goal.pose.position.z = 0.000

    # Set goal orientation (example quaternion)
    goal.pose.orientation.x = 0.0
    goal.pose.orientation.y = 0.0
    goal.pose.orientation.z = -1.0
    goal.pose.orientation.w = 0.0

    pub.publish(goal)
    rospy.loginfo("Goal sent to TurtleBot!")

if __name__ == '__main__':
    try:
        send_goal()
    except rospy.ROSInterruptException:
        pass
