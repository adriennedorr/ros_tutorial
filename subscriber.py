#! /usr/bin/env python3
import rospy
from std_msgs.msg import Float64


def temperature_callback(msg):
    print(msg.data)
    num = msg.data
    if num < 70:
        print('It is cold')
    else:
        print('It is hot')


rospy.init_node('subscriber', anonymous=True)

rospy.Subscriber("/temperature", Float64, temperature_callback)

rospy.spin()
