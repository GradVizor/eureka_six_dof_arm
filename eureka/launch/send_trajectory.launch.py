from launch import LaunchDescription
from launch.substitutions import Command, FindExecutable, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    # Get URDF via xacro
    robot_description_content = Command(
        [
            PathJoinSubstitution([FindExecutable(name="xacro")]),
            " ",
            PathJoinSubstitution(
                [
                    FindPackageShare("eureka"),
                    "urdf",
                    "robot.xacro",
                ]
            ),
        ]
    )
    robot_description = {"robot_description": robot_description_content}

    send_trajectory_node = Node(
        package="eureka",
        executable="send_trajectory",
        name="send_trajectory_node",
        parameters=[robot_description],
    )

    nodes_to_start = [send_trajectory_node]
    return LaunchDescription(nodes_to_start)