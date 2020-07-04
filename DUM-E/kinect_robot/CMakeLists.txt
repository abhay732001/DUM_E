c_make_minimum_required(VERSION 3.0.2)
project(DUM-E)

## Add support for c++11,supported in ROS Kinect and newer
add_definitions(-std=c++11)

#Load catkin and all dependencies required for this package
find_package(catkin REQUIRED COMPONENTS
  rospy
  gazebo_ros
)

#Depend on system install of Gazebo
find_package(gazebo REQUIRED)

link_directories(${GAZEBO_LIBRARY_DIRS})
include_directories(${Boost_INCLUDE_DIR} ${catkin_INCLUDE_DIRS} ${GAZEBO_INCLUDE_DIRS})

catkin_package(
  DEPENDS
   rospy
   gazebo_ros
)