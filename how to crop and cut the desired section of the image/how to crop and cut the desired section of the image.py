#!/usr/bin/env python
# coding: utf-8

# how to crop and cut the desired section of the image 

# In[1]:


# import the required library
import cv2
import numpy as np


# In[6]:


#reading our input image as using imread function
input_image = cv2.imread('Ashish.jpg')
height, width = input_image.shape[:2]

print(height,width)

# extract the pixel coordinate from starting 

start_row , start_col = int(height*0.20),int(width*0.20)

# extract the pixel coordinate from ending bootom 

end_row , end_col = int(height*0.80),int(width*0.80)

# using the indexing method to crop the desired section of the rectangle area


cropped_image = input_image [start_row:end_row,start_col:end_col]
# Display the original and croped image

cv2.imshow('original image',input_image)

cv2.waitKey(0)

cv2.imshow ('cropped_image',cropped_image)

cv2.waitKey(0)

cv2.destroyAllWindows()

