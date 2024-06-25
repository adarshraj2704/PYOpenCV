#!/usr/bin/env python
# coding: utf-8

# In[8]:


# import the required library for the process
import numpy as np
import cv2


# In[14]:


#load the image into classify face variable using the function name CascadeClassifier

classify_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# load input image 
imagedata_original = cv2.imread('Ashish.jpg')
cv2.imshow ('Origianl Image Result ', imagedata_original)
cv2.waitKey(0)

# convert the load image into grayscale image for better identification of face
grayscale_img = cv2.cvtColor(imagedata_original, cv2.COLOR_BGR2GRAY)
cv2.imshow ('Gray Scale image Results ', grayscale_img)
cv2.waitKey(0)

# Region of intrest detected the face ,stored as tuple of the left coordinate and bottom right coordinate 
face_roi = classify_face.detectMultiScale(grayscale_img ,1.3,2)



#check the face is detected or not 
if face_roi is ():
    print("Face are not Detected , please provide another image .")
    


# iterate through face and draw a rectangle over each face    
for (x,y,w,h) in face_roi:
    cv2.rectangle(imagedata_original,(x,y),(x+w,y+h),(127,0,255),2)
cv2.imshow ('Face Detection Results ', imagedata_original)
    
cv2.waitKey(0)
cv2.destroyAllWindows()

