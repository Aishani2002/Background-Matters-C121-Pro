import cv2
import time
import numpy as np

#To save the output in a file output.avi
fourcc = cv2.VideoWriter_fourcc(*"XVID")
outputFile = cv2.VideoWriter("output.avi",fourcc,20.0,(640,480))

#starting the webcam
cap = cv2.VideoCapture(0)

#Allowing the webcam to start by making the code sleep for 2 seconds
time.sleep(2)

bg = 0

#capturing background for 60 frames
for i in range(60):
    ret,bg=cap.read()
bg = np.flip(bg,axis=1)

#reading the captured frame until the camera is open
while (cap.isOpened()):
    ret,img = cap.read()
    if not ret:
        break
    img = np.flip(img,axis=1)
    
    #converting the colour from bgr to hsv
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    #generating mask to detect red color
    l_black = np.array([30,30,0])
    u_black = np.array([104,153,70])
    mask = cv2.inRange(hsv,l_black, u_black)
    
    #open and expand the image when there is mask 1
    mask = cv2.morphologyEx(mask1,cv2.MORPH_OPEN, np.ones((3,3),np.uint8))
    mask = cv2.morphologyEx(mask1,cv2.MORPH_DILATE, np.ones((3,3),np.uint8))
    
    #keeping only the part of the image without the red colour
    res1 = cv2.bitwise_and(img,img,mask = mask)
    
    #keeping only the part of the image with the red colour
    res2 = cv2.bitwise_and(bg,bg,mask = mask)
    
    #generating the final output while merging res1 and res2
    finalOutput = cv2.addWeighted(res1,1,res2,1,0)
    outputFile.write(finalOutput)
    
    #displaying the output to the user
    cv2.imshow(finalOutput)
    cv2.waitKey(1)

#To close the camera
cap.release()
out.release()
cv2.destroyAllWindows()