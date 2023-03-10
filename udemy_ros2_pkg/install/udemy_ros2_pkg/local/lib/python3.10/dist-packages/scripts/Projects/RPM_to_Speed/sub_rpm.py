import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

WHEEL_RADIUS_DEFAULT = 12.5 / 100 # centimeter to meters

class Sub_rpm_node(Node):
    
    def __init__(self):
        super().__init__("sub_rpm")
        self.declare_parameter("wheel_radius", WHEEL_RADIUS_DEFAULT)
        self.sub = self.create_subscription(Float32, "topic_rpm", self.rpm_processor_callback, 10)
        self.pub = self.create_publisher(Float32, "topic_speed", 10)


    def rpm_processor_callback(self, rpm_msg):
        wheel_radius_param = self.get_parameter("wheel_radius").get_parameter_value().double_value
        speed = rpm_msg.data * wheel_radius_param * 2 * 3.14159 / 60 # speed in m/s

        speed_msg = Float32()
        speed_msg.data = float(speed)
        self.pub.publish(speed_msg)


def main():
    rclpy.init()

    sub_rpm_node = Sub_rpm_node()
    print("rpm processor awaiting data...")

    try:
        rclpy.spin(sub_rpm_node)
    except KeyboardInterrupt():
        sub_rpm_node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()