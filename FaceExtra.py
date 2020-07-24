import cv2
import sys
import os

class FaceExtra:
	def __init__(self,path):
		self.path=path

	def faceExtra(self):
		img=cv2.imread(self.path)
		classifier="haarcascade_frontalface_alt.xml"
		hc=cv2.CascadeClassifier(classifier)
		faces=hc.detectMultiScale(img)
		i=1
		for face in faces:
			imgROI = img[face[1]:face[1]+face[3],face[0]:face[0]+face[2]]
			s=self.path
			cv2.imwrite(s,imgROI)
			i=i+1