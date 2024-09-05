import cv2
print(cv2.getVersionString())
image = cv2.imread('opencv_logo.jpg')
cv2.imshow('b',image[:,:,0])
cv2.imshow('g',image[:,:,1])
cv2.imshow('r',image[:,:,2])
#彩图灰度变换算法 BGR三原色的加权平均——反映明暗——cmos接收的光子量
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray)
#裁剪 先横行（高） 再纵列（宽）
crop=image[10:170,50:100]
cv2.imshow('crop' ,crop)
cv2.waitKey()