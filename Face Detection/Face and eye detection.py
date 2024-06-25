#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import the required library for the process
import numpy as np
import cv2


# In[12]:


#load the image into classify face variable using the function name CascadeClassifier

classify_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
classify_eye = cv2.CascadeClassifier ('haarcascade_eye.xml')
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
    gray_crop = grayscale_img[y:y+h,x:x+w]
    color_crop = imagedata_original[y:y+h,x:x+w]
    eyes = classify_eye.detectMultiScale(gray_crop)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(color_crop,(ex,ey),(ex+ew,ey+eh),(127,255,255),2)
        cv2.imshow ('Face with eye ', imagedata_original)
        cv2.imwrite("Ashish.jpg",imagedata_original)
        cv2.waitKey(0)
cv2.destroyAllWindows()

