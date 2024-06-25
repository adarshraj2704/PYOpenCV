#!/usr/bin/env python
# coding: utf-8

# In[3]:


#import required library
import cv2
import numpy as np


# In[8]:


# define two variable which store the mouse press value and mouse position value
draw = False  #it will true when mouse is pressed
ix,iy = -1,-1 # it store the mouse position 

# create a rectangle_shape function to draw a rectangle when mouse is pressed from correct position

def rectangle_shape (event,x,y,warning,par):
    global draw,ix,iy
    
    # checking the event that mouse is clicked orr not 
    if event ==cv2.EVENT_LBUTTONDOWN:
        # change the value of draw from false to true when mouse is draged from the top to down
        draw = True
        #mouse location is saved in the created variable
        ix,iy = x,y
     
    #checking the mouse is draged or not----
    elif event == cv2.EVENT_MOUSEMOVE:
        # if it draged then draw will be set to true
        if draw ==True:
            #if the draw value is true then it means it clicked the mouse left button
            # so the rectangle is created accroding to the given value
            cv2.rectangle (image_window,(ix,iy),(x,y),(255,0,255),-1)
          
    #this event identify the mouse is released and not moving    
    elif event ==cv2.EVENT_LBUTTONUP:
        draw = False
        # so the draw value become false
        #here we complete to draw the rectangle on image window
        cv2.rectangle (image_window,(ix,iy),(x,y),(255,0,255),-1)
            
            
# creating a black image window
image_window = np.zeros((1024,1024,3),np.uint8)

#naming the window reference
cv2.namedWindow(winname='Image_Window')

#connecting the mouse button to the callback function

cv2.setMouseCallback('Image_Window',rectangle_shape)

while True:  # keep the black image window is open untill we press with Esc key
    
    
    # showing the image window
    cv2.imshow('Image_Window',image_window)
    
    #coming out of the window by press Esc key
    if cv2.waitKey(1) & 0xff ==27:
        break
        
cv2.destroyAllWindows()

