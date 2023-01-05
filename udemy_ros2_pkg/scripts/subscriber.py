import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class HelloWorldSubscriber(Node):
    def __init__(self):
        super().__init__("hello_world_sub_node")
        self.sub = self.create_subscription(String, "hello_world", 
                                            self.hello_world_subscriber_callback, 10)

    def hello_world_subscriber_callback(self, msg):
        print("Received: " + msg.data)

def main():
    rclpy.init() # initlaizes DDL services

    my_sub = HelloWorldSubscriber()
    print("Subscriber node running...")

    try:
        rclpy.spin(my_sub)
    except KeyboardInterrupt:
        my_sub.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()