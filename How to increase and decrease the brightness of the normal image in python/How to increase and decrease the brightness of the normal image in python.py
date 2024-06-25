#!/usr/bin/env python
# coding: utf-8

# How to increase and decrease the brightness of the normal image in python

# In[2]:


# import the required library for the process
import cv2
import numpy as np


# In[5]:



# load the original Image in variable 
input_image=cv2.imread('Ashish.jpg')
cv2.imshow('original image',input_image)

#For increasing and decreasing the brightness we have to add matrix and substract  matrix  on the image so the image 
# get more lighten and after substracting the image get more dimed
# so here firstly we have to make a matrix that help in addition and substraction

intensity_matrix = np.ones(input_image.shape,dtype="uint8")*60

# for checking the how much amout of brightness is increase or decrease by printing the intensity matrix

print (intensity_matrix)

# Now , for increasing the brightness of the image we have to add matrix on the original image so that the original image get lighten up
brightened_image = cv2.add(input_image,intensity_matrix)
cv2.imshow('Bright Image',brightened_image)


# Now , for decreasing the brighteness of the image we have substract the intensity matrix from the original image 
darkened_image = cv2.subtract(input_image,intensity_matrix)
cv2.imshow('Dark Image',darkened_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

