# ROS_Publish_Subscribe node model in RaspberryPI Model 3

## Project Overview
Simple Pub/Sub node architecture to control the PWM frequency of an LED in Raspberry Pi. The Publisher node will publish the PWM frequency to the 'stream' topic and the subscriber node will listen to this topic to control the LED.

# Setting up ROS on Raspberry Pi 3 Model B
Follow this [link](http://wiki.ros.org/ROSberryPi/Installing%20ROS%20Kinetic%20on%20the%20Raspberry%20Pi) to install ROS in Raspberry PI. For this project I chose the SD Card Image with Ubuntu 16.04 (LXDE). ROS comes preinstalled with this image.

# Configuring ROS Environment
Follow this [link] (http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment) to setup the ROS environment in Raspberry PI


# LED connections
Connect LED Anode to pin 12 and LED cathode to GND via a 1k resistor.

# Reference
[wiki.ros.org](http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29)
