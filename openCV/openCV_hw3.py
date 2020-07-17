import cv2
import numpy as np
# p1=cv2.VideoCapture("images/homework3.mp4")
c1=cv2.VideoCapture("images/homework3.mp4")

# while c1.isOpened()==True:
#     ret, m1 = c1.read()
#     m2 = cv2.inRange(m1, (100, 30, 20), (200, 80, 55))
#     m2 = cv2.dilate(m2, np.ones((45,45)))
#     # m2 = cv2.erode(m2, np.ones((25,25)))
#     if ret == True:
#         a, b = cv2.findContours(m2,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE) 
#         #cv2.drawContours(m1,contours,-1,(0,0,255),3)  
#         if 0 < len(a):
#             x, y, w, h = cv2.boundingRect(a[0])
#             cv2.rectangle(m1, (x,y), (x + w, y + h), (0, 0, 255), 2)

#         cv2.imshow("output", m1)
#         #cv2.imshow("Image 2", m2)
#         if cv2.waitKey(33)!=-1:
#            break
#     else:
#         break
# cv2.destroyAllWindows()


# 老師講解
mb = np.full((0),255, np.uint)
while c1.isOpened()==True:
	ret, m1=c1.read()
	if ret == True:
		m2 = cv2.cvtColor(m1, cv2.COLOR_BGR2HSV)
		#先取1秒的第一張背景
		if mb.shape[0] == 0:
			mb = m2.copy()
		#正常減背景剩筆的顏色(綠)
		m2 = cv2.subtract(m2, mb)
		#做二質化，因前後明暗度差很大
		th, m2 = cv2.threshold(m2, 127, 255, cv2.THRESH_BINARY)
		#轉灰階音因等要抓輪廓
		m2 = cv2.cvtColor(m2, cv2.COLOR_BGR2GRAY)
		#再二質化把灰色變白色
		th, m2 = cv2.threshold(m2, 127, 255, cv2.THRESH_BINARY)
		#使筆的紅點聚集。讓顏色範圍增大
		m2 = cv2.dilate(m2, np.ones((15,15)))
		#抓輪廓
		a, b = cv2.findContours(m2,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
		# 紅色框抓筆
		for i in range(0, len(a)):
			x, y, w, h = cv2.boundingRect(a[i])
			cv2.rectangle(m1, (x,y), (x+w, y+h), (0, 0, 255), 2)
		
		cv2.imshow("Image 1", m1)
		# 可直接把綠色抓掉，而不需用轉灰階
		cv2.imshow("Image 2", m2[:,:,1])
		if cv2.waitKey(33) != -1:
			break
	else:
		break


cv2.destroyAllWindows()
