import cv2
import numpy as np
import os

def strt():
    os.system('clear')
    print('Welcome to the face detector. Remember to type any character to close the image.')

    path = input('Please type the name of the photo with its extention: ')
    img = cv2.imread(path)

    size_x = float(input('type the value for x resize: '))
    size_y = float(input('Type the value for y resize: '))
    img = cv2.resize(img,(0,0),fx=size_x,fy=size_y)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.3,5)

    for (x,y,width,height) in faces:
        cv2.rectangle(img, (x,y) , (x+width ,y+height) , (255,0,0) ,3)

    cv2.imshow('frame',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()