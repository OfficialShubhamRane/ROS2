import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Sub_rpm_node(Node):

    def __init__(self):
        super().__init__("sub_rpm")
        self.sub = self.create_subscription(String, "/topic_rpm", self.rpm_processor_callback, 10)


    def rpm_processor_callback(self, msg):
        print("received: "+ msg.data)


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