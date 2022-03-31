import numpy as np 
import cv2
import matplotlib.pyplot as plt

img=np.zeros((512,512,3),np.uint8)
pts=np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
pts=pts.reshape((-1,1,2))

cv2.polylines(img, pts, 1, 255)
cv2.fillPoly(img, pts, 255)

cv2.imshow('img',img)
cv2.waitKey(0)