#!/usr/bin/env python
import tf
import rospy

if __name__ == '__main__':

  rospy.init_node('tf_basic_amr')

  # blink is a contraction of base link
  blink_bfprint = tf.TransformBroadcaster()
  bcamera_blink = tf.TransformBroadcaster()

  rate = rospy.Rate(50)

  while not rospy.is_shutdown():

    blink_bfprint.sendTransform((0.00, 0.00, 0.002),
        tf.transformations.quaternion_from_euler(0, 0, 0),
        rospy.Time.now(),"base_link","base_footprint")

    bcamera_blink.sendTransform((0.04, 0.00, 0.00),
        tf.transformations.quaternion_from_euler(0, 0, 0),
        rospy.Time.now(),"front_camera_link","base_link")

    rate.sleep()
