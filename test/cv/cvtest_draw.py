import cv2
import numpy as np
image = np.zeros([300,300,3],dtype=np.uint8)#灰度图
cv2.imshow('draw',image)
#利用cv2画图线 原始图像，起始坐标，终点坐标，颜色，粗细
cv2.line(image,(0,0),(100,200),(0,0,255),3)
#方框 起始，终点，颜色，粗细
cv2.rectangle(image,(20,20),(200,200),(0,255,0),3)
#圆形 圆心，半径，颜色，粗细
cv2.circle(image,(150,150),50,(255,0,0),6)
#文字 图，字，位置，字体序号，缩放系数，颜色，粗细
cv2.putText(image,'Helllllo',(20,250),0,1,(255,255,255),2)
cv2.imshow('draw',image)
cv2.waitKey()