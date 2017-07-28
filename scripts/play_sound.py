#!/usr/bin/env python
# coding=utf-8

import rospy
import rospkg
from std_msgs.msg import String
from wm_sound_library.srv import *
import os
from subprocess import check_call, CalledProcessError

class wm_sound_library:
    def __init__(self, node_name):
        rospy.init_node(node_name)
        s = rospy.Service('wm_play_sound', play_service, self.play)
        rospack = rospkg.RosPack()
        self.packpath = rospack.get_path('wm_sound_library')

    def play(self, req):

        try:
            os.system("aplay " + self.packpath +"/sounds/"+str(req.play.data))

            rospy.loginfo("Sound \"" + str(req.play.data) + "\" was played")
            return True

        except CalledProcessError:
            rospy.logwarn('Last subprocess call was not valid.')
            return False

if __name__ == '__main__':

    try:
        wm_sound_library('wm_sound_library_node')

        rospy.spin()

    except rospy.ROSInterruptException:
        pass
