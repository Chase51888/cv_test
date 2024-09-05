import cv2
import numpy as np
def cv_show(name,image):
    cv2.imshow(name,image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
image1 = cv2.imread('plane.jpg',cv2.IMREAD_GRAYSCALE)
image2=cv2.imread('./cv/test1.jpg',cv2.IMREAD_GRAYSCALE)
imagea=image1/255
imageb=image2/255
imagec=(imagea+imageb)*255
cv2.imshow('c=(a/255+b/255)*255',imagec)
imaged=(imagea*imageb)*255
cv2.imshow('c=(a/255*b/255)*255',imaged)

imagea=cv2.divide(image1,255)
imageb=cv2.divide(image2,255)
imagec=cv2.multiply(image1,image2)
imagec=cv2.multiply(imagec,255)
cv2.imshow('cv:c=(a/255*b/255)*255',imagec)
imaged=cv2.add(imagea,imageb)
imaged=cv2.multiply(imaged,255)
cv2.imshow('cv:c=(a/255+b/255)*255',imagec)
cv2.waitKey()
cv2.destroyAllWindows()