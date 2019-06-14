#impprt libraries
import numpy as np
import os
import pandas as pd
import cv2

face_cascade = cv2.CascadeClassifier('C:\\Users\\admin\\Desktop\\SummerTrainingForsk\\Day 27\\-face_recognition-master\\haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

#give path where you want to save dataset
path = "C:\\Users\\admin\\Desktop\\SummerTrainingForsk\\Day 27\\-face_recognition-master\\dataset\\"

ID=input("Enter users name: ")


try:
    os.mkdir(path+str(ID))
    print("Directory " + path+str(ID) + " Created")
except FileExistsError:
    print("Directory "+ path+str(ID)+ " already exists.")

sampleN=0

while(1):
    ret, img=cap.read()
    frame=img.copy()
    
    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for(x,y,w,h) in faces:
        sampleN+=1
        
        cv2.imwrite( path+str(ID) + "\\" + str(sampleN) + ".jpg", gray[y:y+h,x:x+w])
        
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
        
        cv2.waitKey(100)
        
    cv2.show('img', img)
    
    cv2.waitKey(1)
    
    if(sampleN> 40):
        break
    
        
    
    
    
