#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist, PoseStamped
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib

def send_goal(goal_pose):
    # Create an action client
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)

    rospy.loginfo("Waiting for move_base action server...")
    client.wait_for_server()

    # Create a MoveBaseGoal message
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()

    # Set the goal position and orientation
    goal.target_pose.pose = goal_pose

    # Send the goal and wait for result
    rospy.loginfo("Sending goal...")
    client.send_goal(goal)

    # Wait for the result
    client.wait_for_result()

    # Check the result
    if client.get_state() == actionlib.GoalStatus.SUCCEEDED:
        rospy.loginfo("Goal reached successfully!")
    else:
        rospy.logwarn("Goal failed or was preempted!")

def increase_speed():
    # Adjust the speed dynamically using cmd_vel
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.sleep(1)  # Allow time for the publisher to connect

    move_cmd = Twist()
    
    # Set a higher linear velocity
    move_cmd.linear.x = 1.5  # Forward speed (increase this value for faster movement)
    move_cmd.angular.z = 0.0  # No rotation (straight line)

    rospy.loginfo("Increasing speed and moving robot...")
    
    pub.publish(move_cmd)

def main():
    rospy.init_node('send_goal')

    # Define goal 1 position and orientation
    goal1 = PoseStamped()
    goal1.pose.position.x = 0.655
    goal1.pose.position.y = -0.862
    goal1.pose.position.z = 0.000
    goal1.pose.orientation.x = 0.0
    goal1.pose.orientation.y = 0.0
    goal1.pose.orientation.z = -0.0753
    goal1.pose.orientation.w = 0.658

    # Increase speed before sending goal
    increase_speed()

    # Send goal 1
    send_goal(goal1.pose)

    # Define goal 2 position and orientation
    goal2 = PoseStamped()
    goal2.pose.position.x = -18.155
    goal2.pose.position.y = -8.619
    goal2.pose.position.z = 0.000
    goal2.pose.orientation.x = 0.0
    goal2.pose.orientation.y = 0.0
    goal2.pose.orientation.z = 0.754
    goal2.pose.orientation.w = 0.657

    # Send goal 2 after goal 1 is reached
    send_goal(goal2.pose)

    # Define goal 3 position and orientation
    goal3 = PoseStamped()
    goal3.pose.position.x = -19.046
    goal3.pose.position.y = 4.325
    goal3.pose.position.z = 0.000
    goal3.pose.orientation.x = 0.0
    goal3.pose.orientation.y = 0.0
    goal3.pose.orientation.z = -1.0
    goal3.pose.orientation.w = 0.017

    # Send goal 3 after goal 2 is reached
    send_goal(goal3.pose)

    # Define goal 4 position and orientation
    goal4 = PoseStamped()
    goal4.pose.position.x = -10.463
    goal4.pose.position.y = -8.523
    goal4.pose.position.z = 0.000
    goal4.pose.orientation.x = 0.0
    goal4.pose.orientation.y = 0.0
    goal4.pose.orientation.z = -0.752
    goal4.pose.orientation.w = 0.659

    # Send goal 3 after goal 2 is reached
    send_goal(goal4.pose)

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass