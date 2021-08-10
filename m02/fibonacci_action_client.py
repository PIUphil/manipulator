import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node

from action_tutorials_interfaces.action import Fibonacci


class FibonacciActionClient(Node):

    def __init__(self):
        super().__init__('fibonacci_action_client')
        self.action_client_ = ActionClient(self, Fibonacci, 'fibonacci')  # 액션타입, 액션이름

    def send_goal(self, order):			# order = n번째 항
        goal_msg = Fibonacci.Goal()
        goal_msg.order = order			# 10

        self.action_client_.wait_for_server()
		#return self.action_client_.send_goal_async(goal_msg)		

		#self.send_goal_future_ = self.action_client_.send_goal_async(goal_msg)
        self.send_goal_future_ = self.action_client_.send_goal_async(goal_msg, feedback_callback=self.feedback_callback)

        self.send_goal_future_.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            return

        self.get_logger().info('Goal accepted :)')

        self.get_result_future_ = goal_handle.get_result_async()
        self.get_result_future_.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info('Result: {0}'.format(result.sequence))
        rclpy.shutdown()

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info('Received feedback: {0}'.format(feedback.partial_sequence))


def main(args=None):
    rclpy.init(args=args)

    fibonacci_action_client = FibonacciActionClient()

    #future = fibonacci_action_client.send_goal(10)
    fibonacci_action_client.send_goal(10)

    #rclpy.spin_until_future_complete(fibonacci_action_client, future)
    rclpy.spin(fibonacci_action_client)
    
    #rclpy.shutdown()


if __name__ == '__main__':
    main()
