#!/usr/bin/env python
from sensor_msgs.msg import CompressedImage, Image
from std_msgs.msg import String
import rospy

class RosExampleNode(object):
    def __init__(self):
        self.node_name = "ROS_Example_Node"

        # Write Publishers, please fill in XXX
        self.pub_image_info_string = rospy.Publisher("image_info_string", String, queue_size=1)
        # Write Subscribers, please fill in XXX
        self.sub_image = rospy.Subscriber("XXX", CompressedImage, "XXX", queue_size=1)
        rospy.loginfo("Initialized %s." %(self.node_name))

    def cbImage(self,image_msg):
	#Generate string message
	image_info_string = "Blue yellow line"
	#Publish string message, please fill in XXX
	self.pub_image_info_string."XXX"("XXX")
	


if __name__ == '__main__': 
    rospy.init_node('Ros_example_node',anonymous=False)
    ros_node = RosExampleNode()
    rospy.spin()

