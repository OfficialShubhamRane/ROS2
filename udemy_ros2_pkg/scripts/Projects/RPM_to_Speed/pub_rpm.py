import rclpy

from rclpy.node import Node
from std_msgs.msg import String

class Pub_rpm_node(Node):

    def __init__(self):
        super().__init__("pub_rpm")
        self.pub = self.create_publisher(String,"topic_rpm",10)
        self.timer = self.create_timer(1,self.rpm_callback)

    def rpm_callback(self):
        msg = String()
        msg.data = '10'
        self.pub.publish(msg)


def main():
    rclpy.init() #start DDL

    pub_rpm_node = Pub_rpm_node()
    print("Starting RPM publisher node...")

    try:
        rclpy.spin(pub_rpm_node)
    except KeyboardInterrupt():
        pub_rpm_node.destroy_node()
        rclpy.shutdown()



if __name__ == '__main__':
    main()