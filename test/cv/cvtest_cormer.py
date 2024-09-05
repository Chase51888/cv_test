import cv2
def cv_show(name,image):
    cv2.imshow(name,image)
    cv2.waitKey()
    cv2.destroyAllWindows()
image = cv2.imread('opencv_logo.jpg',cv2.IMREAD_GRAYSCALE)
#gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv_show('test',image)