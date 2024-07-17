# Rony-Temperature-ROS: Temperature Monitoring and Alerting System

This repository implements a ROS 2 system for temperature monitoring and alerting, designed as an assignment for Session 5. It features four interconnected nodes that collaborate to achieve these functionalities:

## Nodes

**1. temperature_meter_node:**

* **Function:** Publishes random temperature values (between 0 and 43 degrees) on the ROS 2 topic named `"temperature"`.

**2. threshold_alerter_node:**

* **Function:** Subscribes to the `"temperature"` topic.
* **Processing:** Analyzes the received temperature data.
* **Alerting:** Publishes messages on the `"alert_trigger"` topic whenever the temperature falls below 15 degrees (considered low) or exceeds 28 degrees (considered high).

**3. alert_publisher_node:**

* **Function:** Subscribes to the `"alert_trigger"` topic.
* **Processing:** Listens for incoming alert messages.
* **Action:** Publishes alerts on the `"alert"` topic whenever an alert message is received on `"alert_trigger"`.

**4. temperature_logger_node:**

* **Function:** Subscribes to the `"temperature"` topic.
* **Logging:** Records every received temperature value to a text file named `"temperature_log.txt"` located in the `src` directory of the package.

## Usage

**1. Prerequisites:**

* A ROS 2 environment set up on your system. Refer to the official ROS 2 documentation for installation instructions: https://docs.ros.org/

**2. Building the Package:**

- Clone the repository to your system:

    ```bash
    git clone https://github.com/RONYkGT/Rony-Temperature-ROS.git
    ```

- Change directory:
    ```bash
    cd Rony-Temperature-ROS/ros2_ws/src/
    ```

- Source ROS2 and the setup.bash file
    ```bash
    source /opt/ros/humble/setup.bash
    ```
    ```bash
    source install/setup.bash
    ```
- Run the package and launch file:
    ```bash
    ros2 launch temperature_monitor temperature_monitor_launch.py
    ```

## System Overview

This system demonstrates how ROS 2 nodes can communicate and collaborate to achieve a specific task. The temperature_meter_node acts as the data source, while the other nodes perform processing and actions based on the received temperature data.

