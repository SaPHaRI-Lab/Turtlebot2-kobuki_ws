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
    move_cmd.linear.x = 2.0  # Forward speed (increase this value for faster movement)
    move_cmd.angular.z = 1.0  # No rotation (straight line)

    rospy.loginfo("Increasing speed and moving robot...")
    
    pub.publish(move_cmd)

def main():
    rospy.init_node('send_goal')

    # Define goal 1 position and orientation
    goal1 = PoseStamped()
    goal1.pose.position.x = -0.309
    goal1.pose.position.y = -5.715
    goal1.pose.position.z = 0.000
    goal1.pose.orientation.x = 0.0
    goal1.pose.orientation.y = 0.0
    goal1.pose.orientation.z = -0.1
    goal1.pose.orientation.w = 0.014

    # Increase speed before sending goal
    increase_speed()

    # Send goal 1
    send_goal(goal1.pose)

    # Define goal 2 position and orientation
    goal2 = PoseStamped()
    goal2.pose.position.x = -1.333
    goal2.pose.position.y = -6.541
    goal2.pose.position.z = 0.000
    goal2.pose.orientation.x = 0.0
    goal2.pose.orientation.y = 0.0
    goal2.pose.orientation.z = -0.738
    goal2.pose.orientation.w = 0.0675

    # Send goal 2 after goal 1 is reached
    send_goal(goal2.pose)

    # Define goal 3 position and orientation
    goal3 = PoseStamped()
    goal3.pose.position.x = -0.897
    goal3.pose.position.y = -7.446
    goal3.pose.position.z = 0.000
    goal3.pose.orientation.x = 0.0
    goal3.pose.orientation.y = 0.0
    goal3.pose.orientation.z = -0.052
    goal3.pose.orientation.w = 0.999

    # Send goal 3 after goal 2 is reached
    send_goal(goal3.pose)

    # Define goal 4 position and orientation
    goal4 = PoseStamped()
    goal4.pose.position.x = 0.004
    goal4.pose.position.y = -7.319
    goal4.pose.position.z = 0.000
    goal4.pose.orientation.x = 0.0
    goal4.pose.orientation.y = 0.0
    goal4.pose.orientation.z = 0.729
    goal4.pose.orientation.w = 0.64

    # Send goal 3 after goal 2 is reached
    send_goal(goal4.pose)

        # Define goal 4 position and orientation
    goal5 = PoseStamped()
    goal5.pose.position.x = -0.309
    goal5.pose.position.y = -5.715
    goal5.pose.position.z = 0.000
    goal5.pose.orientation.x = 0.0
    goal5.pose.orientation.y = 0.0
    goal5.pose.orientation.z = -1
    goal5.pose.orientation.w = 0.014

    # Send goal 3 after goal 2 is reached
    send_goal(goal5.pose)

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass