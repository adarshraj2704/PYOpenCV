#!/usr/bin/env python
# coding: utf-8

# # image sharpening depend on the 2 factors 
# 1. Resolution
# 2.Acutance

# What are the needs of Sharpening the image
#       1. to overcome Blurring in the images
#       2. to Highlight certain areas of the image
#       3. to increase the legibilty 

# In[1]:


# import the Required Library for the process

import cv2
import numpy as np


# In[3]:



# store the input image in the variable 
imagedata= cv2.imread('Ashish.JPG')
cv2.imshow('Original Image',imagedata)
cv2.waitKey(0)


# create a sharpening kernel 

sharpening_filter = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])



# Applying kernel to the input image to get image more sharpened image
sharpened_image = cv2.filter2D(imagedata,-1,sharpening_filter)
cv2.imshow('Sharpened Image',sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

