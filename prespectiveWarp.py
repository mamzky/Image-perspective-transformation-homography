#IMAGE TRANSFORMATION

import cv2
import numpy as np

#Read Image
img = cv2.imread('stat.png')
height, width = img.shape[:2]
cv2.imshow("Original", img)

#Prespective transformation
#                   x  y    x   y   x    y     x   y
pts1 = np.float32([[0,0],[0,100],[100,100],[100,0]])
#pts2 = np.float32([[158,100],[63,100],[7,11],[193,11]])
pts2 = np.float32([[360,90],[17,512],[590,510],[540,90]])
M_presp = cv2.getPerspectiveTransform(pts1,pts2)
print ("Computed prespective transform matrix : ")
print (M_presp)
print (img.shape[:2])

img_presp = cv2.warpPerspective(img,M_presp, (960,540))
cv2.imshow("Prespective transform", img_presp)

cv2.waitKey(0)
