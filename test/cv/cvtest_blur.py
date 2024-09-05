import cv2
image = cv2.imread('plane.jpg')
cv2.imshow('blur1',image)
#高斯滤波器 图，内核，sigma
gauss=cv2.GaussianBlur(image,(5,5),0)
cv2.imshow('blur2',gauss)
#中值滤波器 一般工作中只用中值足够用
median=cv2.medianBlur(image,5)
cv2.imshow('blur3',median)
cv2.waitKey()