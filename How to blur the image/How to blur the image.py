#!/usr/bin/env python
# coding: utf-8

# Blur the image

# In[1]:


# import the required Library
import cv2
import numpy as np


# In[2]:


# load the input image in Image data

imagedata= cv2.imread('Ashish.jpg')
cv2.imshow('originalImage',imagedata)
cv2.waitKey(0)


kernel_size = np.ones((5,5),np.float32) /25

blurred_Image = cv2.filter2D(imagedata,-1,kernel_size)
cv2.imshow('kernal Size Image ', blurred_Image)
cv2.waitKey(0)


kernal_Size_9x9= np.ones((9,9),np.float32)/81
blurred_Image2 = cv2.filter2D(imagedata,-1,kernal_Size_9x9)
cv2.imshow('kernal Size Image ', blurred_Image2)
cv2.waitKey(0)


# Other Method Are also listed below

# In[7]:


import cv2
import numpy as np

image_data =cv2.imread('Ashish.jpg')

# Using Gaussion Filter
gaussian_blur = cv2.GaussianBlur(image_data,(7,7),0)
cv2.imshow('Guassian Blur ', gaussian_blur)
cv2.waitKey(0)


# In[4]:


avg_blur = cv2.blur(imagedata,(3,3))
cv2.imshow('Average Blur ', avg_blur)
cv2.waitKey(0)


# In[5]:


# Median Blur

median_blur = cv2.medianBlur(imagedata,5)
cv2.imshow('median Blur ', median_blur)
cv2.waitKey(0)

