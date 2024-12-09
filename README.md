# Turtlebot2: kobuki_ws
Contains all necessary packages for the Turtlebot2 on ROS Noetic.

Also custom built for Jetson -> Pi overhaul, LiDAR, MQTT communication, and rviz.

Documentation for the entire project is currently private.

## For the Master:
`.master.py` is an executable for the master computer--functioning as the broker and mastermind of the Turtlebot swarm.

## For the Turtlebots (Pis):
Run `setup_pi` first, then use `minimal_ext.launch` instead of `minimal.launch` to boot.
