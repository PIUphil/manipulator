#!/usr/bin/env python3

import rclpy

from pick_and_place.get_kinematics import KinematicsSubscriber
from pick_and_place.joint_control import JointController

from getkey import getkey


def main(args=None):
    rclpy.init(args=args)

    kinematics_subscriber = KinematicsSubscriber()
    joint_controller = JointController()

    command = ''
    # 명령어를 받는다 -> 특정 command -> kinematics_sub -> 프로그램 종료
    #              -> 그 외 command -> joint_controller
    #print("lets go")
    while True:
        print("Please insert command : ", end='')
        command = getkey()
        if command == '1':
            #print(command)
            while len(kinematics_subscriber.get_kinematics_position()) == 0:
                rclpy.spin_once(kinematics_subscriber)
            print(kinematics_subscriber.get_kinematics_position())
            print(kinematics_subscriber.get_kinematics_orientation())
            break
        else:
            #print(command, "hi")
            joint_controller.send_command(command)
            rclpy.spin_once(joint_controller)

    kinematics_subscriber.destroy_node()
    joint_controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
