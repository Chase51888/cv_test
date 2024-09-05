import cv2
import numpy as np

image=cv2.imread('./cv/m2.jpg',cv2.IMREAD_GRAYSCALE)
image= cv2.resize(image,(300,300),cv2.INTER_AREA)

cv2.imwrite('./cv/test_m2.jpg',image)
