#!/usr/bin/python
import cv2
import sys
import os
if __name__ == "__main__" :

            imagename="contrast.jpg"
            img=cv2.imread(imagename)
            # if (img==None):
            # print("File not found") # Or not readable?
            # sys.exit()
    
        #create haar cascade classifier
            path="haarcascade_frontalface_alt.xml"
        #path = "/usr/share/opencv/haarcascades/haarcascade_frontalface_alt2.xml"
            hc=cv2.CascadeClassifier(path)    
            # if (hc.empty()):
            #   print("CascadeClassifer could not be loaded")
            #   sys.exit()

        #detect faces
            faces=hc.detectMultiScale(img)
            i=1
            for face in faces:
              imgROI = img[face[1]:face[1]+face[3],face[0]:face[0]+face[2]]
            #imgROI = img[face[1]-25:face[1]+face[3]+25, 
            #             face[0]-20:face[0]+face[2]+20]
              s=imagename
              cv2.imwrite(s,imgROI)
              i=i+1

            print(str(i-1)+" face(s) extracted")            
