#!/usr/bin/env python3

import rospy
import os, time
from playsound import playsound
from geometry_msgs.msg import Twist, PoseStamped
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib

audio_file = os.path.expanduser('~/kobuki_ws/src/turtlebot/turtlebot_bringup/assets/quack.mp3')

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
        playsound(audio_file)
    else:
        rospy.logwarn("Goal failed or was preempted!")

def increase_speed():
    # Adjust the speed dynamically using cmd_vel
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.sleep(1)  # Allow time for the publisher to connect

    move_cmd = Twist()
    
    # Set a higher linear velocity
    move_cmd.linear.x = 3.0  # Forward speed (increase this value for faster movement)
    move_cmd.angular.z = 0.5  # No rotation (straight line)

    rospy.loginfo("Increasing speed and moving robot...")
    
    pub.publish(move_cmd)

def chester():
    try:
        # Lead node 1
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

        # Lead node 2
        goal2 = PoseStamped()
        goal2.pose.position.x = -12.293
        goal2.pose.position.y = -8.258
        goal2.pose.position.z = 0.000
        goal2.pose.orientation.x = 0.0
        goal2.pose.orientation.y = 0.0
        goal2.pose.orientation.z = -0.999
        goal2.pose.orientation.w = 0.047

        # Send goal 2 after goal 1 is reached
        send_goal(goal2.pose)

        # Front Door
        goal3 = PoseStamped()
        goal3.pose.position.x = -19.209
        goal3.pose.position.y = 4.171
        goal3.pose.position.z = 0.000
        goal3.pose.orientation.x = 0.0
        goal3.pose.orientation.y = 0.0
        goal3.pose.orientation.z = -0.999
        goal3.pose.orientation.w = 0.034

        send_goal(goal3.pose)
        time.sleep(1)

        # Personal Space
        goal4 = PoseStamped()
        goal4.pose.position.x = -17.987
        goal4.pose.position.y = 4.379
        goal4.pose.position.z = 0.000
        goal4.pose.orientation.x = 0.0
        goal4.pose.orientation.y = 0.0
        goal4.pose.orientation.z = -1.0
        goal4.pose.orientation.w = 0.026

        send_goal(goal4.pose)
        time.sleep(2)

        # Dr. Block Room
        goal5 = PoseStamped()
        goal5.pose.position.x = -9.782
        goal5.pose.position.y = -8.414
        goal5.pose.position.z = 0.000
        goal5.pose.orientation.x = 0.0
        goal5.pose.orientation.y = 0.0
        goal5.pose.orientation.z = -0.996
        goal5.pose.orientation.w = 0.093

        send_goal(goal5.pose)
        time.sleep(4)

        # Audio
        # Maybe an additional audio file here, playing a quack when we arrive at every destination >:)

        # Come back to my desk
        goal6 = PoseStamped()
        goal6.pose.position.x = 0.230
        goal6.pose.position.y = -0.228
        goal6.pose.position.z = 0.000
        goal6.pose.orientation.x = 0.0
        goal6.pose.orientation.y = 0.0
        goal6.pose.orientation.z = 0.006
        goal6.pose.orientation.w = 1.0

        send_goal(goal6.pose)
    except Exception as e:
        rospy.logerr(f'Exception when moving around SaPHaRI: {e}')
        return -1
    return 0

if __name__ == '__main__':
    try:
        chester()
    except rospy.ROSInterruptException:
        pass