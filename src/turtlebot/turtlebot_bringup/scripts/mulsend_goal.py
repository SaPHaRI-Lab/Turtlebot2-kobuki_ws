#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseStamped
import heapq

def cost(current, neighbor):
    return 1  # Assuming each step has a uniform cost of 1

def convert_to_grid_index(position, grid_resolution=1.0):
    """
    Convert the (x, y) real-world coordinates to the closest grid index
    based on the given grid resolution.
    """
    x, y = position
    grid_x, grid_y = int(round(x / grid_resolution)), int(round(y / grid_resolution))

    # Debugging: log the conversion
    rospy.loginfo(f"Converted real-world coordinates {position} to grid indices ({grid_x}, {grid_y})")
    
    return grid_x, grid_y

def a_star(start, goal, grid):
    open_list = []
    heapq.heappush(open_list, (0 + heuristic(start, goal), start))
    came_from = {}
    g_score = {start: 0}
    
    while open_list:
        _, current = heapq.heappop(open_list)
        
        if current == goal:
            return reconstruct_path(came_from, current)
        
        for neighbor in get_neighbors(current, grid):
            tentative_g = g_score[current] + cost(current, neighbor)
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_score, neighbor))
                came_from[neighbor] = current
    return None

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan distance

def get_neighbors(pos, grid):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    neighbors = []
    for dx, dy in directions:
        nx, ny = pos[0] + dx, pos[1] + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0:
            neighbors.append((nx, ny))
    return neighbors

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

def send_goal(x, y):
    pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
    rospy.sleep(1)  # Allow time for the node to initialize

    goal = PoseStamped()
    goal.header.frame_id = "map"
    goal.header.stamp = rospy.Time.now()
    goal.pose.position.x = x
    goal.pose.position.y = y
    goal.pose.orientation.w = 1.0  # Facing forward

    pub.publish(goal)
    rospy.loginfo(f"Goal sent to ({x}, {y})")

def convert_to_grid_index(position, grid_resolution=1.0):
    """
    Convert the (x, y) real-world coordinates to the closest grid index
    based on the given grid resolution.
    """
    x, y = position
    return int(round(x / grid_resolution)), int(round(y / grid_resolution))

def main():
    rospy.init_node('a_star_path_sender')

    # Define starting point and goals in real-world coordinates
    start_real = (0.146, -0.111)  # Starting point (x, y)
    goals_real = [
        (-6.087, -7.811),  # Goal 1
        (-18.155, -8.619), # Goal 2
        (-19.046, 4.325)   # Goal 3
    ]

    # Define the grid as a 2D list (assuming free spaces = 0, obstacles = 1)
    grid = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ]

    # Convert real-world coordinates to grid indices
    start = convert_to_grid_index(start_real)
    goals = [convert_to_grid_index(goal) for goal in goals_real]

    # Start from the initial position
    current_position = start

    # Process each goal in the list
    for goal in goals:
        rospy.loginfo(f"Calculating path to goal {goal}")
        path = a_star(current_position, goal, grid)
        
        if path:
            for waypoint in path:
                send_goal(waypoint[0], waypoint[1])
                rospy.sleep(2)  # Allow time for the robot to move to each goal
            current_position = goal  # Update the current position after reaching each goal
        else:
            rospy.loginfo(f"No path found to goal {goal}")
    
    rospy.loginfo("All goals completed!")

if __name__ == '__main__':
    main()