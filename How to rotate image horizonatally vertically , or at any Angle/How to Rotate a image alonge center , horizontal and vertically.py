#!/usr/bin/env python
# coding: utf-8

# In[5]:


#import requiredd Library for the process
import cv2
import numpy as np


#store the image in any variable

input_image = cv2.imread('Ashish.jpg')
cv2.imshow('original Image',input_image)


# here we try to know the height and weidth of the image for the rotation 
height , width = input_image.shape[:2]

# for rotation we use the function name getRotationMatrix2D and rotate the image through its center by using the height and width
rotation = cv2.getRotationMatrix2D((width/2,height/2),45,0.5)

rotate_image_output = cv2.warpAffine(input_image , rotation,(width,height))

cv2.imshow('Rotated Image',rotate_image_output)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Rotation of the image horizontal

# In[10]:


horizontal_image = cv2.flip(input_image,1)
cv2.imshow('Horizontal Flipped Image ', horizontal_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Rotation of the image vertically

# In[11]:


vertical_image = cv2.flip(input_image,0)
cv2.imshow('vertically Flipped Image ', vertical_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

