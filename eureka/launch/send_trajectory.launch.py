from launch import LaunchDescription
from launch.substitutions import Command, FindExecutable, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from ament_index_python.packages import get_package_share_directory
import xacro
import os

def generate_launch_description():
    # Get URDF via xacro
    share_dir = get_package_share_directory('eureka')
    xacro_file = os.path.join(share_dir, 'urdf', 'robot.xacro')
    robot_description_config = xacro.process_file(xacro_file)
    robot_description_content = robot_description_config.toxml()
    robot_description = {"robot_description": robot_description_content}

    send_trajectory_node = Node(
        package="eureka",
        executable="send_trajectory",
        name="send_trajectory_node",
        parameters=[robot_description],
    )

    nodes_to_start = [send_trajectory_node]
    return LaunchDescription(nodes_to_start)
