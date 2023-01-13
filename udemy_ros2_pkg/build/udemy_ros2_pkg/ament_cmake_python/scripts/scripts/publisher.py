#! /usr/bin/env python3
import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class HelloWorldPublisher(Node):
    def __init__(self):
        super().__init__("hello_world_pub_node")
        self.pub = self.create_publisher(String, "hello_world", 10)
        self.timer = self.create_timer(2, self.hello_world_callback)

    def hello_world_callback(self):
        msg = String()
        msg.data = "Hello world"
        self.pub.publish(msg)


def main():
    rclpy.init()

    hello_world_pub = HelloWorldPublisher()
    print("Publisher node running...")

    try:
        rclpy.spin(hello_world_pub)
    except KeyboardInterrupt:
        hello_world_pub.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()