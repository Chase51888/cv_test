import cv2
import numpy as np
def cv_show(name,image):
    cv2.imshow(name,image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
image = cv2.imread('plane.jpg',cv2.IMREAD_GRAYSCALE)
squre_result=np.square(image)
cv2.imshow('squre',squre_result)

log_result=image
log_image=np.astype(log_result,np.float32)
print(type(log_image))
log_result=np.log(log_image+1)
log_result=cv2.normalize(log_result,None,0,255,cv2.NORM_MINMAX)
log_result= log_result.astype(np.uint8)
cv2.imshow('log',log_result)



cv2.waitKey()
cv2.destroyAllWindows()