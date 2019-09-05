#IMAGE TRANSFORMATION

import cv2
import numpy as np

#Read Image
img = cv2.imread('framePuriMall.png')
height, width = img.shape[:2]
cv2.imshow("Original", img)

#Translation
M_trans = np.float32(
    [[1,0,100],[0,1,50]])
print ("Translation matrix :")
print (M_trans)
img_trans = cv2.warpAffine(img, M_trans, (width,height))
cv2.imshow("Translation", img_trans)
cv2.waitKey(0)
