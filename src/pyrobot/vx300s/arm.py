# Copyright (c) Facebook, Inc. and its affiliates.

# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.


import numpy as np
import rospy

from pyrobot.core import Arm


class vx300sArm(Arm):
    """
    This class has functionality to control a vx300s manipulator.
    """

    def __init__(self, configs, moveit_planner="RRTConnect"):
        """
        The constructor for LoCoBotArm class.

        :param configs: configurations read from config file
        :param moveit_planner: Planner name for moveit,
                               only used if planning_mode = 'moveit'.
        :type configs: YACS CfgNode
        :type moveit_planner: string
        """
        super(vx300sArm, self).__init__(
            configs=configs, moveit_planner=moveit_planner, use_moveit=True
        )

    def go_home(self):
        """
        Commands robot to home position
        """
        self.set_joint_positions(np.zeros(self.arm_dof), plan=True)

    def move_to_neutral(self):
        """
        Move the robot to a pre-defined neutral pose
        """

        # TODO: Change it to some better neutral position
        neutral_pos = [0, -1.7, -1.6, 0.0015, -1.110, -0.006]
        self.set_joint_positions(neutral_pos, plan=True)

    def _setup_joint_pub(self):
        rospy.loginfo("Setting up the joint publishers")

    def _pub_joint_positions(self, positions):
        raise NotImplementedError

    def _pub_joint_velocities(self, velocities):
        raise NotImplementedError("Velocity control for " "vx300s not supported yet!")

    def _pub_joint_torques(self, torques):
        raise NotImplementedError("Torque control for " "vx300s is not supported yet!")

    def set_joint_velocities(self, velocities, **kwargs):
        raise NotImplementedError("Velocity control for " "vx300s not supported yet!")

