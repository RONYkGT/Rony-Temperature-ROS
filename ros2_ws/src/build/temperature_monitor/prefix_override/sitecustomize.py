import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/rony/Documents/inmind/Session05/Rony-Temperature-ROS/ros2_ws/src/install/temperature_monitor'
