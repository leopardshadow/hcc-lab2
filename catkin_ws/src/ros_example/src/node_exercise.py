#!/usr/bin/env python
from sensor_msgs.msg import CompressedImage, Image
from std_msgs.msg import String
import rospy

class RosExerciseNode(object):
    def __init__(self):
        self.node_name = "ROS_Exercise_Node"

        # Write Publishers
        self.pub_image_info_string_reply = rospy.Publisher("~image_info_string_reply", String, queue_size=1)
        # Write Subscribers
        self.sub_image_info_string = rospy.Subscriber("~image_info_string", String, self.cbString, queue_size=1)
       
        rospy.loginfo("Initialized %s." %(self.node_name))

    def cbString(self,image_msg):
	#Generate string messag
	image_info_string =  "This is " + image_msg.data
	#Publish string message
	self.pub_image_info_string_reply.publish(image_info_string)
	


if __name__ == '__main__': 
    rospy.init_node('Ros_exercise_node',anonymous=False)
    ros_node = RosExerciseNode()
    rospy.spin()

