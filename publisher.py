#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64

# generate random floating point values
from random import seed
from random import random

# seed random number generator
seed(1)
# generate random numbers between 0-1
for _ in range(100):
    value = random()

rospy.init_node('publisher', anonymous=True)
pub = rospy.Publisher('/temperature', Float64, queue_size=10)

while not rospy.is_shutdown():
    temperature_msg = Float64()
    temperature_msg.data = value#*100.
    pub.publish(temperature_msg)
    rospy.sleep(1)
