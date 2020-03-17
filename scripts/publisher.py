#!/usr/bin/env python


import rospy
from std_msgs.msg import String
i=0;
def publish():
	global i;
	pub = rospy.Publisher('stream',String,queue_size=10)
	rospy.init_node('send',anonymous=True)
	rate = rospy.Rate(3)
	while not rospy.is_shutdown():
		mess = "Set PWM Freq: " + str(i) + " Hz";
		i=i+1;
		if(i==50):
			i=1;
		rospy.loginfo(mess)
		pub.publish(str(i));
		rate.sleep()

if __name__=='__main__':
	try:
		publish()
	except rospy.ROSInterruptException:
		pass