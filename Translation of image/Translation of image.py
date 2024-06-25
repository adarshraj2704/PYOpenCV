#!/usr/bin/env python
# coding: utf-8

# In[2]:


# import required library for the process
import cv2
import numpy as np


# In[ ]:


# store the image in variable to use it 
input_image = cv2.imread('Ashish.jpg')

# show the stored original image
cv2.imshow('Original Image', input_image)

# obtained the height and width of the image 
# we use parameter in last is [2] because we only want height and width not color
height,width =input_image.shape[:2]
print(height,width)
print("=============")

# set how much translation you want 
tx, ty = height/8,width/8

# creating the translation matrix using the above tx and ty value
t=np.float32([[1,0,tx],[0,1,ty]])

print (t)


translation = cv2.warpAffine(input_image,t,(width,height))

# showing the image output

cv2.imshow('translation Image',translation)
cv2.waitKey()
cv2.destroyAllWindows()



# In[ ]:




