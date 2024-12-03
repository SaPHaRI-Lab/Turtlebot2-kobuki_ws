# Install script for directory: /home/SaPHaRI/kobuki_ws/src

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/SaPHaRI/kobuki_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  
      if (NOT EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}")
        file(MAKE_DIRECTORY "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}")
      endif()
      if (NOT EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/.catkin")
        file(WRITE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/.catkin" "")
      endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/SaPHaRI/kobuki_ws/install/_setup_util.py")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/SaPHaRI/kobuki_ws/install" TYPE PROGRAM FILES "/home/SaPHaRI/kobuki_ws/build/catkin_generated/installspace/_setup_util.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/SaPHaRI/kobuki_ws/install/env.sh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/SaPHaRI/kobuki_ws/install" TYPE PROGRAM FILES "/home/SaPHaRI/kobuki_ws/build/catkin_generated/installspace/env.sh")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/SaPHaRI/kobuki_ws/install/setup.bash;/home/SaPHaRI/kobuki_ws/install/local_setup.bash")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/SaPHaRI/kobuki_ws/install" TYPE FILE FILES
    "/home/SaPHaRI/kobuki_ws/build/catkin_generated/installspace/setup.bash"
    "/home/SaPHaRI/kobuki_ws/build/catkin_generated/installspace/local_setup.bash"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/SaPHaRI/kobuki_ws/install/setup.sh;/home/SaPHaRI/kobuki_ws/install/local_setup.sh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/SaPHaRI/kobuki_ws/install" TYPE FILE FILES
    "/home/SaPHaRI/kobuki_ws/build/catkin_generated/installspace/setup.sh"
    "/home/SaPHaRI/kobuki_ws/build/catkin_generated/installspace/local_setup.sh"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/SaPHaRI/kobuki_ws/install/setup.zsh;/home/SaPHaRI/kobuki_ws/install/local_setup.zsh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/SaPHaRI/kobuki_ws/install" TYPE FILE FILES
    "/home/SaPHaRI/kobuki_ws/build/catkin_generated/installspace/setup.zsh"
    "/home/SaPHaRI/kobuki_ws/build/catkin_generated/installspace/local_setup.zsh"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/SaPHaRI/kobuki_ws/install/.rosinstall")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/SaPHaRI/kobuki_ws/install" TYPE FILE FILES "/home/SaPHaRI/kobuki_ws/build/catkin_generated/installspace/.rosinstall")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/SaPHaRI/kobuki_ws/build/gtest/cmake_install.cmake")
  include("/home/SaPHaRI/kobuki_ws/build/freenect_stack/freenect_launch/cmake_install.cmake")
  include("/home/SaPHaRI/kobuki_ws/build/freenect_stack/freenect_stack/cmake_install.cmake")
  include("/home/SaPHaRI/kobuki_ws/build/kobuki/kobuki/cmake_install.cmake")
  include("/home/SaPHaRI/kobuki_ws/build/kobuki/kobuki_capabilities/cmake_install.cmake")
  include("/home/SaPHaRI/kobuki_ws/build/kobuki/kobuki_rapps/cmake_install.cmake")
  include("/home/SaPHaRI/kobuki_ws/build/turtlebot/turtlebot/cmake_install.cmake")
  include("/home/SaPHaRI/kobuki_ws/build/turtlebot_apps/turtlebot_apps/cmake_install.cmake")
  include("/home/SaPHaRI/kobuki_ws/build/turtlebot/turtlebot_bringup/cmake_install.cmake")
  include("/home/SaPHaRI/kobuki_ws/build/turtlebot/turtlebot_capabilities/cmake_install.cmake")
  include("/home/SaPHaRI/kobuki_ws/build/turtlebot_simulator/turtlebot_gazebo/cmake_install.cmake")
  include("/home/SaPHaRI/kobuki_ws/build/turtlebot_apps/turtlebot_rapps/cmake_install.cmake")
  include("/home/SaPHaRI/kobuki_ws/build/turtlebot_simulator/turtlebot_simulator/cmake_install.cmake")
  include("/home/SaPHaRI/kobuki_ws/build/turtlebot_simulator/turtlebot_stage/cmake_install.cmake")
  include("/home/SaPHaRI/kobuki_ws/build/turtlebot_simulator/turtlebot_stdr/cmake_install.cmake")
  include("/home/SaPHaRI/kobuki_ws/build/kobuki/kobuki_keyop/cmake_install.cmake")
  include("/home/SaPHaRI/kobuki_ws/build/kobuki/kobuki_auto_docking/cmake_install.cmake")
  include("/home/SaPHaRI/kobuki_ws/build/freenect_stack/freenect_camera/cmake_install.cmake")
  include("/home/SaPHaRI/kobuki_ws/build/kobuki/kobuki_bumper2pc/cmake_install.cmake")
  include("/home/SaPHaRI/kobuki_ws/build/rplidar_ros/cmake_install.cmake")
  include("/home/SaPHaRI/kobuki_ws/build/turtlebot_apps/turtlebot_actions/cmake_install.cmake")
  include("/home/SaPHaRI/kobuki_ws/build/turtlebot_apps/turtlebot_calibration/cmake_install.cmake")
  include("/home/SaPHaRI/kobuki_ws/build/turtlebot_msgs/cmake_install.cmake")
  include("/home/SaPHaRI/kobuki_ws/build/turtlebot_apps/turtlebot_follower/cmake_install.cmake")
  include("/home/SaPHaRI/kobuki_ws/build/turtlebot_apps/turtlebot_navigation/cmake_install.cmake")
  include("/home/SaPHaRI/kobuki_ws/build/turtlebot/turtlebot_teleop/cmake_install.cmake")
  include("/home/SaPHaRI/kobuki_ws/build/kobuki/kobuki_description/cmake_install.cmake")
  include("/home/SaPHaRI/kobuki_ws/build/turtlebot/turtlebot_description/cmake_install.cmake")
  include("/home/SaPHaRI/kobuki_ws/build/yujin_ocs/yocs_cmd_vel_mux/cmake_install.cmake")
  include("/home/SaPHaRI/kobuki_ws/build/yujin_ocs/yocs_controllers/cmake_install.cmake")
  include("/home/SaPHaRI/kobuki_ws/build/kobuki/kobuki_controller_tutorial/cmake_install.cmake")
  include("/home/SaPHaRI/kobuki_ws/build/kobuki/kobuki_random_walker/cmake_install.cmake")
  include("/home/SaPHaRI/kobuki_ws/build/kobuki/kobuki_safety_controller/cmake_install.cmake")
  include("/home/SaPHaRI/kobuki_ws/build/yujin_ocs/yocs_velocity_smoother/cmake_install.cmake")
  include("/home/SaPHaRI/kobuki_ws/build/kobuki/kobuki_node/cmake_install.cmake")
  include("/home/SaPHaRI/kobuki_ws/build/kobuki/kobuki_testsuite/cmake_install.cmake")

endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/SaPHaRI/kobuki_ws/build/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
