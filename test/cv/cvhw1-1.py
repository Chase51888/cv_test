import cv2
import numpy as np
import math as mt
def cv_show(name,image):
    cv2.imshow(name,image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image = cv2.imread('plane.jpg',cv2.IMREAD_GRAYSCALE)
'''target_width=300
target_height=300
target_size=(target_width,target_height)
image=cv2.resize(image,target_size,cv2.INTER_AREA)
cv2.imwrite('./cv/test1.jpg',image)'''

#print(image.shape)
image_2=cv2.imread('./cv/test1.jpg',cv2.IMREAD_GRAYSCALE)
#cv_show('Test',image)
add_result=cv2.add(image_2,image_2)
#add_result=image+128
#cv_show('Add',add_result)
image_3=cv2.imread('./cv/test_m1.jpg',cv2.IMREAD_GRAYSCALE)
image_4=cv2.imread('./cv/test_m2.jpg',cv2.IMREAD_GRAYSCALE)
sub_result=cv2.subtract(image_3,image_4)
sub_result=cv2.subtract(image,image)

#cv_show('Sub',sub_result)
cv2.imshow('Original',image)
cv2.imshow('Add',add_result)
add_result=cv2.add(image_2,image_2)
add_result=cv2.add(image_2,image_2)
add_result=cv2.add(image_2,image_2)
cv2.imshow('Add_3times',add_result)
cv2.imshow('Sub',sub_result)
image_5=cv2.imread('./cv/test3.jpg',cv2.IMREAD_GRAYSCALE)
#mul2_result=cv2.multiply(image_2,3)
mul2_result=image_2*3
#cv_show('Mul',mul2_result)
div2_result=cv2.divide(image_5,2)
cv2.imshow('Mul2',mul2_result)
cv2.imshow('Div2',div2_result)
#gxy=a fxy+b

image_5=cv2.multiply(image_5,1.5)
cv2.imshow('3f',image_5)
image_5=cv2.add(image_5,50)
cv2.imshow('3f+5',image_5)



cv2.waitKey(0)

cv2.destroyAllWindows()
