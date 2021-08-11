#!/usr/bin/env python3

from rclpy.node import Node
from open_manipulator_msgs.msg import KinematicsPose

class KinematicsSubscriber(Node):
    def __init__(self):
        super().__init__('kinematics_subscriber')

        self.subscription = self.create_subscription(KinematicsPose, 'kinematics_pose', self.kinematics_callback, 10)
        self.subscription   # 오류가 날 수 있어서 한번더 써넣음..?

        self.kinematics_position = []
        self.kinematics_orientation = []

    def kinematics_callback(self, msg: KinematicsPose):     # msg의 type적어줘도됨
        tmp_position_list = []
        tmp_orientation_list = []

        tmp_position_list.append(msg.pose.position.x)
        tmp_position_list.append(msg.pose.position.y)
        tmp_position_list.append(msg.pose.position.z)

        tmp_orientation_list.append(msg.pose.orientation.x)
        tmp_orientation_list.append(msg.pose.orientation.y)
        tmp_orientation_list.append(msg.pose.orientation.z)
        tmp_orientation_list.append(msg.pose.orientation.w)

        self.kinematics_position = tmp_position_list.copy()
        self.kinematics_orientation = tmp_orientation_list.copy()

    def get_kinematics_position(self):
        return self.kinematics_position

    def get_kinematics_orientation(self):
        return self.kinematics_orientation





