#!/usr/bin/env python3

from rclpy.node import Node

from open_manipulator_msgs.srv import SetJointPosition


class JointController(Node):
    def __init__(self):
        super().__init__('joint_control')

        self.client = self.create_client(SetJointPosition, 'goal_joint_space_path_from_present')
        self.request = SetJointPosition.Request()

        self.joint_delta = 0.05
        self.path_time = 0.5

    def send_command(self, command: str):
        # q/a/w/s/e/d/r/f  -> 1,2,3,4번 조인트값을 상승/하강
        if command is 'q':
            # joint 1번값 올리기
            joint_name = []
            joint_angle = []

            joint_name.append("joint1")
            joint_name.append("joint2")
            joint_name.append("joint3")
            joint_name.append("joint4")

            joint_angle.append(self.joint_delta)
            joint_angle.append(0.0)
            joint_angle.append(0.0)
            joint_angle.append(0.0)

            self.set_joint_control(joint_name, joint_angle)

        elif command is 'a':
            # joint 1번값 내리기
            joint_name = []
            joint_angle = []

            joint_name.append("joint1")
            joint_name.append("joint2")
            joint_name.append("joint3")
            joint_name.append("joint4")

            joint_angle.append(self.joint_delta * -1.0)
            joint_angle.append(0.0)
            joint_angle.append(0.0)
            joint_angle.append(0.0)

            self.set_joint_control(joint_name, joint_angle)

        elif command is 'w':
            # joint 2번값 올리기
            joint_name = []
            joint_angle = []

            joint_name.append("joint1")
            joint_name.append("joint2")
            joint_name.append("joint3")
            joint_name.append("joint4")

            joint_angle.append(0.0)
            joint_angle.append(self.joint_delta)
            joint_angle.append(0.0)
            joint_angle.append(0.0)

            self.set_joint_control(joint_name, joint_angle)

        elif command is 's':
            # joint 2번값 내리기
            joint_name = []
            joint_angle = []

            joint_name.append("joint1")
            joint_name.append("joint2")
            joint_name.append("joint3")
            joint_name.append("joint4")

            joint_angle.append(0.0)
            joint_angle.append(self.joint_delta * -1.0)
            joint_angle.append(0.0)
            joint_angle.append(0.0)

            self.set_joint_control(joint_name, joint_angle)

        elif command is 'e':
            # joint 3번값 올리기
            joint_name = []
            joint_angle = []

            joint_name.append("joint1")
            joint_name.append("joint2")
            joint_name.append("joint3")
            joint_name.append("joint4")

            joint_angle.append(0.0)
            joint_angle.append(0.0)
            joint_angle.append(self.joint_delta)
            joint_angle.append(0.0)

            self.set_joint_control(joint_name, joint_angle)

        elif command is 'd':
            # joint 3번값 내리기
            joint_name = []
            joint_angle = []

            joint_name.append("joint1")
            joint_name.append("joint2")
            joint_name.append("joint3")
            joint_name.append("joint4")

            joint_angle.append(0.0)
            joint_angle.append(0.0)
            joint_angle.append(self.joint_delta * -1.0)
            joint_angle.append(0.0)

            self.set_joint_control(joint_name, joint_angle)

        elif command is 'r':
            # joint 4번값 올리기
            joint_name = []
            joint_angle = []

            joint_name.append("joint1")
            joint_name.append("joint2")
            joint_name.append("joint3")
            joint_name.append("joint4")

            joint_angle.append(0.0)
            joint_angle.append(0.0)
            joint_angle.append(0.0)
            joint_angle.append(self.joint_delta)

            self.set_joint_control(joint_name, joint_angle)

        elif command is 'f':
            # joint 4번값 내리기
            joint_name = []
            joint_angle = []

            joint_name.append("joint1")
            joint_name.append("joint2")
            joint_name.append("joint3")
            joint_name.append("joint4")

            joint_angle.append(0.0)
            joint_angle.append(0.0)
            joint_angle.append(0.0)
            joint_angle.append(self.joint_delta * -1.0)

            self.set_joint_control(joint_name, joint_angle)

    def set_joint_control(self, joint_name: list, joint_angle: list):
        self.request.joint_position.joint_name = joint_name
        self.request.joint_position.position = joint_angle
        self.request.path_time = self.path_time

        future = self.client.call_async(self.request)
