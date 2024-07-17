import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
from random import randint

class TemperatureMeter(Node):
    def __init(self):
        super().__init__("temperature_meter")
        self.publisher_ = self.create_publisher(String, "temperature", 10)
        timer_period = 1
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Int16()
        msg.data = randint(0, 43)
        self.publisher_.publish(msg)
        self.get_logger().info("Publishing: %d" % msg.data)
        

def main(args=None):
    rclpy.init(args=args)
    temperature_meter = TemperatureMeter()
    rclpy.spin(temperature_meter)
    temperature_meter.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

        