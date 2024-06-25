#!/usr/bin/env python
# coding: utf-8

# Image Masking

# In[5]:


# import required library
import cv2
import numpy as np


# In[6]:


square_image = np.zeros((400,400,1),np.uint8)
cv2.rectangle(square_image,(75,75),(300,300),255,-2)
cv2.imshow("Square",square_image)
cv2.waitKey(0)


circle = np.zeros((400,400,1),np.uint8)
cv2.circle(circle,(300,300),75,(255,0,0),-1)
cv2.imshow("circle",circle)
cv2.waitKey(0)
cv2.destroyAllWindows()


# BitWise Operation for image masking on shape

# In[7]:


# Showing the region wherw both square and circle intersect
And_Operation = cv2.bitwise_and(square_image,circle)
cv2.imshow('And Operation ',And_Operation)
cv2.waitKey(0)


# Showing the region where either Square or circle is intersect
Or_Operation = cv2.bitwise_or(square_image,circle)
cv2.imshow('Or Operation ',And_Operation)
cv2.waitKey(0)


# Showing the region where either Square or circle is exixts
xOr_Operation = cv2.bitwise_xor(square_image,circle)
cv2.imshow('xOr Operation ',xOr_Operation)
cv2.waitKey(0)

# Showing the region that isn't part of sqaure 
Not_Operation = cv2.bitwise_not(square_image,circle)
cv2.imshow('Not Operation ',Not_Operation)
cv2.waitKey(0)

cv2.destroyAllWindows()

