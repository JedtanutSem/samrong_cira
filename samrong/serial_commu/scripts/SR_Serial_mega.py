#!/usr/bin/env python

import serial
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import time
import json
max_linear_speed = 0.5
max_angular_speed = 1
vel_x = 0

pwmL = 0
pwmR = 0
dirL = 0
dirR = 0

get_1 = 0
get_2 = 0
get_3 = 0
get_4 = 0
get_5 = 0
get_6 = 0

def cira_send_clbk(data):
    global get_1,get_2,get_3,get_4,get_5,get_6
    str_get = data.data
    json_acceptable_string = str_get.replace("'", "\"")
    get_dict = json.loads(json_acceptable_string)
    get_1 = get_dict['out1']
    get_2 = get_dict['out2']
    get_3 = get_dict['out3']
    get_4 = get_dict['out4']
    get_5 = get_dict['out5']
    get_6 = get_dict['out6']

if __name__ == "__main__":

    rospy.init_node('read_ser', anonymous=True)
    rospy.Subscriber("cira_send",String, cira_send_clbk)
    pub_in = rospy.Publisher("cira_get",String,queue_size=10)
    rate = rospy.Rate(10) # 10hz
    try:
        arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        #rospy.Subscriber('chatter', String, callback)
        #rospy.loginfo("test")

        while not rospy.is_shutdown():
            #ospy.loginfo("loop")
            str = '%s,%s,%s,%s,%s,%s,' %(get_1,get_2,get_3,get_4,get_5,get_6)#pwm_L, dir_L, pwm_R, dir_R
            #rospy.loginfo(str)
            arduino.write(str)
            data = arduino.readline()[:-2]

            rospy.loginfo(data)
            pub_in.publish(data)
            rate.sleep()
    except Exception as e:
        rospy.loginfo("Serial Fail")
        print e

