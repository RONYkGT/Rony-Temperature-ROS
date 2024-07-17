from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='temperature_monitor',
            executable='temperature_meter_node',
            name='temperature_meter_node'
        ),
        Node(
            package='temperature_monitor',
            executable='threshold_alerter_node',
            name='threshold_alerter_node'
        ),
        Node(
            package='temperature_monitor',
            executable='alert_publisher_node',
            name='alert_publisher_node'
        ),
    ])
