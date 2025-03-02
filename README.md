# Eureka (6 D.O.F.)
Eureka is a 6 degree of freedom robotic arm designed to perform tasks like painting, examine, welding, surgeries and simple pick n place. It utilizes *ROS2*, *Rviz2* for simulation, and implemented *MoveIt2* for planning and execution of any task. I've implemented control with the help of *ros2_control* features for precise motor control (made custom hardware interface).

![Eureka in Action](eureka/resource/eureka.mp4)

## Table of Contents
1) Features

2) Directory Structure

3) Getting Started 

## Features
1) Achieves accurate movements as it uses KDL library for calculating inverse kinematics.

2) Easily add custom tools such as grippers, cameras, or sensors.

3) Simulation environment is Rviz2 for testing algorithms.

4) Custom ros2_control hardware interfaces for precise motor control.


## Directory Structure

```
eureka/
|-- config/
|   |-- display.rviz
|   |-- eureka_controller.yaml
|
|-- controller/
|   |-- include/          
|   |   |-- eureka/    
|   |   |   |-- eureka_controller.hpp  
|   |-- eureka_controller.cpp   
|
|-- eureka/
|   |-- __init__.py
|
|-- hardware/
|   |-- include/      
|   |   |-- eureka/
|   |   |   |-- eureka_hardware.hpp
|   |-- eureka_hardware.cpp
|
|-- launch/
|   |-- display.launch.py
|   |-- eureka_controller.launch.py
|   |-- gazebo.launch.py
|   |-- rsp.launch.py
|   |-- send_trajectory.launch.py
|
|-- meshes/ 
|   |-- base_link.stl
|   |-- link1.stl
|   |-- link2.stl
|   |-- link3.stl
|   |-- link4.stl
|   |-- link5.stl
|   |-- link6.stl
|   |-- link7a.stl
|   |-- link7b.stl
|
|-- resource/
|   |-- eureka
|
|-- src/              
|   |-- command_test.cpp
|   |-- send_trajectory.cpp
|
|-- urdf/
|   |-- material.xacro
|   |-- robot.gazebo
|   |-- robot.trans
|   |-- robot.xacro
|   |-- ros2_control.xacro
|
|-- CMakeLists.txt
|
|-- eureka.xml
|
|-- package.xml


eureka_moveit/
|-- config/
|
|-- launch/
|   |-- demo.launch.py
|
|-- src/
|   |-- first.cpp
|
|-- .setup_assistant
|
|-- CMakeLists.txt
|
|-- package.xml
```


## Getting Started
1) Clone the repository:-
   
   `https://github.com/GradVizor/eureka_six_dof_arm.git` 
   
2) Make sure to install required packages and dependencies by checking out eureka/package.xml.

3) Build your project:
   
   Ensure your build system includes the necessary source files and header paths. 
   

