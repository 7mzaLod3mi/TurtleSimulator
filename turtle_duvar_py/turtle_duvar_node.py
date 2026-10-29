
import math
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist


class TurtleNode(Node):

    def __init__(self):
        super().__init__('turtle_duvar_node')

        self.declare_parameter('speed', 2.0)
        self.declare_parameter('minLimit', 1.0)
        self.declare_parameter('maxLimit', 10.0)

        self.speed = self.get_parameter('speed').value
        self.minLimit = self.get_parameter('minLimit').value
        self.maxLimit = self.get_parameter('maxLimit').value

        self.x = 5.5
        self.y = 5.5
        self.theta = 0.0
        self.firstPose = False
        self.lastLog = self.get_clock().now()

        self.subscriber = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.readPose,
            10
        )

        self.publisher = self.create_publisher(
            Twist,
            '/turtle1/cmd_vel',
            10
        )

        self.timer = self.create_timer(0.1, self.moveTurtle)

    def readPose(self, msg):
        self.x = msg.x
        self.y = msg.y
        self.theta = msg.theta
        self.firstPose = True

    def moveTurtle(self):
        if not self.firstPose:
            return

        now = self.get_clock().now()

        if (now - self.lastLog).nanoseconds >= 1000000000:
            self.get_logger().info(
                f'x: {self.x:.2f}, y: {self.y:.2f}'
            )
            self.lastLog = now

        cmd = Twist()

        nearWall = (
            self.x < self.minLimit + 0.5
            or self.x > self.maxLimit - 0.5
            or self.y < self.minLimit + 0.5
            or self.y > self.maxLimit - 0.5
        )

        if nearWall:
            target = math.atan2(5.5 - self.y, 5.5 - self.x)
            difference = target - self.theta

            while difference > math.pi:
                difference = difference - 2 * math.pi

            while difference < -math.pi:
                difference = difference + 2 * math.pi

            if abs(difference) > 0.15:
                if difference > 0:
                    cmd.angular.z = 1.5
                else:
                    cmd.angular.z = -1.5
            else:
                cmd.linear.x = self.speed
        else:
            cmd.linear.x = self.speed

        self.publisher.publish(cmd)


def main(args=None):
    rclpy.init(args=args)
    node = TurtleNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.publisher.publish(Twist())
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

