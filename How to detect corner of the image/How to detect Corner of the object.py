#!/usr/bin/env python
# coding: utf-8

# How to detect Corner of the object

# In[3]:


import cv2
import numpy as np


# In[4]:


imagedata = cv2.imread('chess.png')
cv2.imshow('Original Image',imagedata)
cv2.waitKey(0)

grayscale = cv2.cvtColor(imagedata,cv2.COLOR_BGR2GRAY)

grayscale = np.float32(grayscale)

harr_corner_info = cv2.cornerHarris(grayscale,3,3,0.05)

kernel = np.ones((7,7),np.uint8)
harr_corner_info = cv2.dilate(harr_corner_info,kernel,iterations =2)

imagedata [harr_corner_info > 0.025 * harr_corner_info.max() ] = [255,0,255]

cv2.imshow('Corner of the image' , imagedata)
cv2.waitKey(0)
cv2.destroyAllWindows()

