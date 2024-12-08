#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def shake_head():
    rospy.init_node('shake_head', anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.sleep(1)  # Allow time for the publisher to connect

    twist = Twist()
    rate = rospy.Rate(10)  # 10 Hz

    # Define the head-shaking parameters
    angular_speed = 1.0  # rad/s (adjust for speed)
    shake_duration = 1.0  # seconds to rotate to one side
    repetitions = 3  # Number of head shakes (left-right pairs)

    rospy.loginfo("Shaking head...")
    for _ in range(repetitions):
        # Rotate to the left
        twist.angular.z = angular_speed
        start_time = rospy.Time.now()
        while (rospy.Time.now() - start_time).to_sec() < shake_duration:
            rate.sleep()

        # Rotate to the right
        twist.angular.z = -angular_speed
        start_time = rospy.Time.now()
        while (rospy.Time.now() - start_time).to_sec() < shake_duration:
            rate.sleep()

    # Stop the robot
    twist.angular.z = 0.0
    pub.publish(twist)
    rospy.loginfo("Head shake completed!")

if __name__ == '__main__':
    try:
        shake_head()
    except rospy.ROSInterruptException:
        pass