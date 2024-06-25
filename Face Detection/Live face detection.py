#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import the required library for the process
import numpy as np
import cv2


# In[ ]:


#load the image into classify face variable using the function name CascadeClassifier

classify_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
classify_eye = cv2.CascadeClassifier ('haarcascade_eye.xml')

# function to detect the face and eye in real time using webcamera 
def detect_face_and_eyes (img, size = 0.5):
    grayscaling = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face_roi = classify_face.detectMultiScale(grayscaling,1.3,5)
    if face_roi is ():
        return img
    
    for (x,y,w,h)  in face_roi:
        x=x-50
        w= w+50
        y=y-50
        h=h+50
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)
        gray_crop = grayscaling[y:y+h,x:x+w]
        color_crop = img[y:y+h,x:x+w]
        eyes = classify_eye.detectMultiScale(gray_crop)
        
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(color_crop,(ex,ey),(ex+ew,ey+eh),(0,255,255),2)
            
            
    color_crop = cv2.flip(color_crop,1)
    return color_crop


cap = cv2.VideoCapture(0)

while True :
    ret, frame = cap.read()
    cv2.imshow('live face detection ', detect_face_and_eyes(frame))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
        
cap.release()
cv2.destroyAllWindows()

