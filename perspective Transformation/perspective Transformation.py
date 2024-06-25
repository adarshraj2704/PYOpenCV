#!/usr/bin/env python
# coding: utf-8

# In[6]:


# import the required library
import cv2
import numpy as np
import matplotlib.pyplot as plt


# In[14]:


# store the image in a variable
input_image =cv2.imread('SamplePage.jpeg')


# In[15]:


# show the original image 
cv2.imshow('original Image',input_image)
cv2.waitKey(0)


# In[16]:


#  write Cordinator of the four corner of the image 

original_coordinate = np.float32([[119,89],[849,73],[47,1153],[903,1173]])

for x in range (0,4):
    cv2.circle(input_image,(original_coordinate[x][0],original_coordinate[x][1]),5,(255,0,255),-1)


# show the marked coordinate of the image
cv2.imshow('coordinated image',input_image)
cv2.waitKey(0)
    


# In[18]:


# making the height under which image is show
height,width = 1024,1024

# coordinate of the 4 corner of the target output
new_image = np.float32([[0,0],[width,0],[0,height],[width,height]])

# use the two sets of four points to compute the prespective transformation mstrix , p 

p= cv2.getPerspectiveTransform(original_coordinate,new_image)

perspective = cv2.warpPerspective(input_image,p,(width,height))

cv2.imshow('final results',perspective)
cv2.waitKey(0)
cv2.destroyAllWindows()



