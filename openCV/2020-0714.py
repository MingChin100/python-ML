import cv2
import numpy as np


m1=cv2.imread("images/3.png", 1)
#cv2.THRESH_OTSU 只接受灰階
# m2=m1.copy()
# th, m2[:,:,0]=cv2.threshold(m1[:,:,0], 50, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
# print(th)
# th, m2[:,:,1]=cv2.threshold(m1[:,:,1], 50, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
# print(th)
# th, m2[:,:,2]=cv2.threshold(m1[:,:,2], 50, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
# print(th)
# m2=cv2.adaptiveThreshold(
# 	m1,
# 	255,
# 	cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
# 	cv2.THRESH_BINARY,
# 	11,
# 	0
# )

# m2=cv2.Canny(m1,100,200)
# m2=cv2.blur(m1,(15,25))
# m2=cv2.medianBlur(m1,155)
# m2=m1.copy()
# m2[:,:,0]=cv2.equalizeHist(m1[:,:,0])
# m2[:,:,1]=cv2.equalizeHist(m1[:,:,1])
# m2[:,:,2]=cv2.equalizeHist(m1[:,:,2])

# m2=cv2.erode(m1, np.ones((5,3)))
# m2=cv2.dilate(m1, np.ones((10,10)))
# m2=cv2.erode(m1, np.ones((3,3)))
# m2=cv2.morphologyEx(m1, cv2.MORPH_GRADIENT, np.ones((5,5)))
# m2=cv2.inRange(m1, (230,230,230), (255,255,255))
# m2=cv2.erode(m2, np.ones((5,20)))
# m2=cv2.inRange(m1, (0,0,255), (0,0 ,255))
# m3=np.full(m1.shape,255,np.uint8)
# a, b=cv2.findContours(m2,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# print(a)
# print(b)

# cv2.imshow("Image 1 ", m1)
# cv2.imshow("Image 2 ", m2)

# for i in range(0,len(a)):
# 	x, y, w, h =cv2.boundingRect(a[i])
# 	if w>10:
# 		# cv2.drawContours(m3,a,i,(0,0,255),2)
# 		cv2.imshow("Image 3"+str(i), m1[y:y+h,x:x+w])
# 		cv2.imwrite("images/"+str(i)+".png", m1[y:y+h,x:x+w])
		# cv2.waitKey(0)

# cv2.imshow("Image 1 B", m1[:,:,0])
# cv2.imshow("Image 1 B", m1[:,:,1])
# cv2.imshow("Image 1 B", m1[:,:,2])
# m2=cv2.inRange(m1, (0,0,0), (120,120,120))
# m2=cv2.erode(m2, np.ones((2,2)))
# m2=cv2.dilate(m2, np.ones((12,12)))
# m2=cv2.cvtColor(m2,cv2.COLOR_GRAY2BGR)
# m2=cv2.add(m1,m2)
# m2=cv2.inRange(m2, (240,240,240), (255,255,255))
# m2=cv2.erode(m2, np.ones((13,15)))
# a, b=cv2.findContours(m2,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# x, y, w, h =cv2.boundingRect(a[1])

# cv2.imshow("Image 1 ", m1)
# # cv2.imshow("Image 1 LOGO ", m1[y:y+h,x:x+w])
# # cv2.imwrite("images/1.png ", m1[y:y+h,x:x+w])
# cv2.imshow("Image 2 ", m2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

m2=cv2.inRange(m1,(240,240,240),(255,255,255))
m2=cv2.erode(m2,np.ones((2,15)))
a, b=cv2.findContours(m2,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
m3=np.full(m1.shape,255,np.uint8)
for i in range(0,len(a)):
	x, y, w, h =cv2.boundingRect(a[i])
	# if w>h*15:
	# 	cv2.rectangle(m3,(x,y),(x+w,y+h).(0,0,255),2)
	m3=cv2.inRange(m1[y:y+h,x:x+w], (32,69,220), (72,109,255))
	m3=cv2.dilate(m, np.ones((5,12)))
	c, d=cv2.findContours(m3,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
	if len(c) ==4:
		cv2.imwrite("images/"+str(i)+".png",m1[y:y+h,x:x+w])


cv2.imshow("Image 1", m1)
cv2.imshow("Image 2", m2)
cv2.imshow("Image 3", m3)

cv2.waitKey(0)
cv2.destroyAllWindows()

