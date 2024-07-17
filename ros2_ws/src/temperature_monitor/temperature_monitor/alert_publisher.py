import rclpy
from std_msgs.msg import String, Int16
from rclpy.node import Node

class AlertPublisher(Node):
    def __init__(self):
        super().__init__("alert_publisher")
        self.publisher_ = self.create_publisher(String,'alert',10)
        self.subscriber_ = self.create_subscription(Int16, 'alert_trigger',self.alert_callback,10)
    
    def alert_callback(self,msg):
        msg = String()
        msg.data = "Alert, bad temperature!"
        self.publisher_.publish(msg)
        self.get_logger().info("Alert published")

def main(args=None):
    rclpy.init(args=args)
    alert_publisher = AlertPublisher()
    rclpy.spin(alert_publisher)
    alert_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

        