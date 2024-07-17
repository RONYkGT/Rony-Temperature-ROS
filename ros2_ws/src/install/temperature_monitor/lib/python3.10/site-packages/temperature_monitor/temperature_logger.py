import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class TemperatureLogger(Node):
    def __init__(self):
        super().__init__('temperature_logger')
        self.subscriber_ = self.create_subscription(Int16,'temperature',self.temperature_callback,10)
        self.f = open("temperature_log.txt", "w")
        self.f.write("Temperature: \n")
    
    def temperature_callback(self, msg):
        self.f.write(str(msg.data) + "\n")

    def __del__(self):
        self.f.close()

def main(args=None):
    rclpy.init(args=args)
    temperature_logger = TemperatureLogger()
    rclpy.spin(temperature_logger)
    temperature_logger.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()