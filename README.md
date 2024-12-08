# Turtlebot2: kobuki_ws
Contains all necessary packages for the Turtlebot2 on ROS Noetic.

Custom-built for mapping, LiDAR, and MQTT communication.

## For the Master:
`.master.py` is an executable for the master computer--functioning as the broker and mastermind of the Turtlebot swarm.

## For the Turtlebots (Pis):
Run `setup_pi` first, then use `minimal_ext.launch` instead of `minimal.launch` to boot.