#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import the required library for the process
import cv2
import numpy as np


# In[2]:


# loading the image in variable 
image_data= cv2.imread('Flower.jpg',0)
cv2.imshow('original Image',image_data)
cv2.waitKey(0)
cv2.destroyAllWindows

# creating the object of the blob dectrors
detectorobj=cv2.SimpleBlobDetector_create()

# passing the object 
keypoint_info = detectorobj.detect(image_data)

# creating the blank image on which the output result is open
blank_img = np.zeros((1,1))

# using the drawKey function to gain the output
blobs = cv2.drawKeypoints(image_data,keypoint_info,np.array([]),(255,0,255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('bLOB',blobs)
cv2.waitKey(0)
cv2.destroyAllWindows

