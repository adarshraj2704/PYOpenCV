#!/usr/bin/env python
# coding: utf-8

# In[11]:



#import the required library
import cv2
import numpy as np


# store the nature image in input_image variable
input_image = cv2.imread('nature.jpg')

cv2.imshow ('original Image',input_image)
cv2.waitKey()

# here use the inbuilt resize function to resize the image Size smaller by 50%
scaled_image = cv2.resize(input_image, None , fx=0.5 ,fy=0.5)
cv2.imshow('scaled Image',scaled_image)
cv2.waitKey()

# here use the inbuilt resize function to resize the image Size largerr by 150%
Larged_image = cv2.resize(input_image, None , fx=1.5 ,fy=1.5)
cv2.imshow('Larged Image',Larged_image)
cv2.waitKey()

# here use the inbuilt resize function to resize the image Size by own given value
scaled_image3 = cv2.resize(input_image,(700,200), interpolation = cv2.INTER_AREA)
cv2.imshow('scaling by input',scaled_image3)
cv2.waitKey()

cv2.destroyAllWindows()


# Image Pyramid

# In[14]:


#import Necessary Library
import cv2

# store the nature image in input_image
input_image = cv2.imread('nature.jpg')


# use the function pyrDown function from the library to decrease the size of the image 
smaller_image = cv2.pyrDown(input_image)

# use the function pyrUp to increase the size of the image 
larger_image = cv2.pyrUp(input_image)

cv2.imshow('original',input_image)

cv2.imshow('smaller image',smaller_image)

cv2.imshow('larger image',larger_image)

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




