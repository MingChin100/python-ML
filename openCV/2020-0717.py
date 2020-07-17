import pytesseract as pt
import numpy as np
import cv2
from pyzbar import pyzbar

# m1 = cv2.imread("images/12.png", 1)
# ret=pt.image_to_string(m1, "AAA", "")
# print(ret)


# cv2.imshow("Image 1", m1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# m1 = cv2.imread("images/2.png", 1)
# m2=cv2.inRange(m1,(240,240,240),(255,255,255))
# m2=cv2.erode(m2,np.ones((2,15)))
# a, b=cv2.findContours(m2,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# m3=np.full(m1.shape,255,np.uint8)
# for i in range(0,len(a)):
# 	x, y, w, h =cv2.boundingRect(a[i])
# 	m3=cv2.inRange(m1[y:y+h,x:x+w], (32,69,220), (72,109,255))
# 	m3=cv2.dilate(m, np.ones((5,12)))
# 	c, d=cv2.findContours(m3,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# 	if len(c) ==4:
# 		m4 = m1[y:y+h, x:x+w]
# 		h = 50
# 		w = int((h/m4.shape[0])*m4.shape[1])
# 		m4 = cv2.resize(m4, (w,h))
# 		m5 = np.full((m4.shape[0]+100, m4.shape[1]+100, 3), 255, np.uint8)
# 		m5[50:m4.shape[0]+50, 50:m4.shape[1]+50] = m4

# 		ret = pt.image_to_string(m5, "eng", "-c tessedit_char_whitelist=T")
# 		print(ret)
# 		cv2.imwrite("output/"+str(i)+".png",m5)
# 		cv2.imshow("Image 4"+str(i), m5)


# cv2.imshow("Image 1", m1)
# cv2.imshow("Image 2", m2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# m1 = cv2.imread("images/13.png", 1)


# c1=cv2.VideoCapture(0)
# while c1.isOpened()==True:
#     ret2, m1 = c1.read()
# if ret2 == True:
# 	ret= pyzbar.decode(m1)
# 	for d in ret:
# 		print("條碼類型:" ,d.type)
# 		try:
# 			print("條碼內容:" ,d.data.decode("utf8"))
# 		except:
# 			print("條碼內容:" ,d.data.decode("utf8").encode("sjis").decode("utf8"))
# 		x,y,w,h=d.rect
# 		cv2.rectangle(m1, (x,y), (x+w,y+h),(0,0,255), 2)
# 		print("=====================================")

# 	cv2.imshow("Image 1", m1)
# 	if cv2.waitKey(0)!= -1:
# 		break
	# else:
		# break
# cv2.destroyAllWindows()

# m1 = cv2.imread("images/12.jpg", 1)
# control=cv2.CascadeClassifier("cascade/haarcascade_frontalface_default.xml")

# returnA=control.detectMultiScale(
# 	m1,
# 	minNeighbors=3,
# 	minSize=(10,10)
# )
# for x,y,w,h in returnA:
# 	cv2.rectangle(m1, (x,y), (x+w, y+h), (0,0,255), 2)
# cv2.imshow("Image 1", m1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


c1=cv2.VideoCapture(0)
control=cv2.CascadeClassifier("cascade/haarcascade_frontalface_default.xml")
while c1.isOpened()==True:
    ret2, m1 = c1.read()
	if ret2 == True:

	returnA=control.detectMultiScale(
		m1,
		minNeighbors=3,
		minSize=(10,10)
)
	for x,y,w,h in returnA:
		cv2.rectangle(m1, (x,y), (x+w, y+h), (0,0,255), 2)
		if cv2.waitKey(0)!= -1:
			break
	else:
		break
cv2.destroyAllWindows()
