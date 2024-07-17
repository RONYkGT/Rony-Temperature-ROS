import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class ThresholdAlerter(Node):
    def __init__(self):
        super().__init__('threshold_alerter')
        self.publisher_ = self.create_publisher(Int16, 'alert_trigger', 10)
        self.subscriber_ = self.create_subscription(Int16,'temperature',self.temp_warning_callback)
    
    def temp_warning_callback(self, msg):
        if msg.data > 28:
            self.publisher_.publish(msg)
            self.get_logger().info('Temperature is too high!')
        elif msg.data < 15:
            self.publisher_.publish(msg)
            self.get_logger().info('Temperature is too low!')
    
def main(args=None):
    rclpy.init(args=args)
    threshold_alerter = ThresholdAlerter()
    rclpy.spin(threshold_alerter)
    threshold_alerter.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

        