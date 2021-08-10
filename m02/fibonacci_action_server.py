import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node

from action_tutorials_interfaces.action import Fibonacci


class FibonacciActionServer(Node):

    def __init__(self):
        super().__init__('fibonacci_action_server')
        self.action_server_ = ActionServer(self, Fibonacci, 'fibonacci', self.execute_callback)

    def execute_callback(self, goal_handle):		# 액션서버가 실행될때 실행되는 함수
        self.get_logger().info('Executing goal...')
        
        sequence = [0, 1]
        
        for i in range(1, goal_handle.request.order):
            sequence.append(sequence[i-1] + sequence[i])

        goal_handle.succeed()

        result = Fibonacci.Result()
        result.sequence = sequence
        return result


def main(args=None):
    rclpy.init(args=args)

    fibonacci_action_server = FibonacciActionServer()

    rclpy.spin(fibonacci_action_server)


if __name__ == '__main__':
    main()
