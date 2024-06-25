#!/usr/bin/env python
# coding: utf-8

# In[4]:


#import the required library
import cv2
import numpy as np

# store the image in local variable
imagedata_original = cv2.imread('car.jpg',0)

# Extract Sobel Edges
sobel_edg_x = cv2.Sobel(imagedata_original,cv2.CV_64F,0,1,ksize=5)
sobel_edg_y = cv2.Sobel(imagedata_original,cv2.CV_64F,1,0,ksize=5)

# Display Images
cv2.imshow('original',imagedata_original)
cv2.waitKey(0)

cv2.imshow('Sobel X',sobel_edg_x)
cv2.waitKey(0)

cv2.imshow('Sobel y',sobel_edg_y)
cv2.waitKey(0)

# Apply Or Operation
Or_operation = cv2.bitwise_or(sobel_edg_x,sobel_edg_y)
cv2.imshow('or operation',Or_operation)
cv2.waitKey(0)

# Laplacian Edge Detection
laplacian_edg_det = cv2.Laplacian(imagedata_original,cv2.CV_64F)
cv2.imshow('LAplacian Edge Detection',laplacian_edg_det)
cv2.waitKey(0)

# Canny Edge Detection
canny_edg = cv2.Canny(imagedata_original,30,180)
cv2.imshow('Canny Edge Detection', canny_edg)
cv2.waitKey(0)

cv2.destroyAllWindows()

