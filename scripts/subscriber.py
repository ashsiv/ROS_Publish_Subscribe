#!/usr/bin/env python


import rospy
from std_msgs.msg import String
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)
p = GPIO.PWM(12,1)
p.start(50);

def callback(data):
	global p;
	rospy.loginfo("Received PWM value:  %s Hz", data.data)
 	freq = int(data.data)
	p.ChangeFrequency(freq);

def listen():
	rospy.init_node('receive',anonymous=True)
	rospy.Subscriber('stream',String,callback)
	rospy.spin()


if __name__=='__main__':
	listen()