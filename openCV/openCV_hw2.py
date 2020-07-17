import cv2
import numpy as np
# from PIL import ImageFont, ImageDraw, Image

m1=cv2.imread("images/homework2.png", 1)
# for h in range(m1.shape[0]):
#     for w in range(m1.shape[1]):
#         if m1[h][w][0] == 0 and \
#            m1[h][w][1] == 0 and \
#            m1[h][w][2] == 255:
#             m1[h][w][0] = 0
#             m1[h][w][1] = 0
#             m1[h][w][2] = 0
#         else:
#             m1[h][w][0] = 255
#             m1[h][w][1] = 255
#             m1[h][w][2] = 255
#自己寫法
# m2=np.full(m1.shape, [0, 0, 255], np.uint8)
# m3=np.full(m1.shape, 255, np.uint8)
# m4=m1[:,:,1]
# m5=m1[:,:,2]

# m6=cv2.absdiff(m5, m4)
# # m7=cv2.multiply(m6, m4)
# m7=cv2.bitwise_not(m6)
# m8=cv2.add(m7,m4)

#老師寫法
#R-G-B
m1[:,:,1]=cv2.substract(m1[:,:,2], m1[:,:,1])
m2=cv2.substract(m1[:,:,2], m1[:,:,0])
#不要都讓它變0,讓文字變1,所以-254[1,0,0],後面再所有的*255,[255,0,0]
m2=cv2.substract(m2, np.full(m2.shape, 254, np.uint8))
m2=cv2.substract(m2, np.full(m2.shape, 255, np.uint8))
#反轉變[0,0,255]
m2=cv2.bitwise_not(m2)

cv2.imshow("Image 2", m2)
cv2.waitKey(0)
cv2.destroyAllWindows()