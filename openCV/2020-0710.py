import cv2
import numpy as np

# m1=cv2.imread("images/XXX.png", 1)
# # m1=cv2.cvtColor(m1, cv2.COLOR_BGR2GRAY)
# # cv2.imwrite("images/XXX.png", m1, [cv2.IMWRITE_JPEG_QUALITY, 10])

# print(m1.shape)
# cv2.imshow("Image 1", m1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# p1=cv2.VideoCapture("images/1.mp4")
# print("高:", p1.get(4))
# print("寬:", p1.get(3))
# print("總影格:", )p1.get(7)
# print("FPS:", p1.get(5))

# p1.set(1, 300)
# f=cv2.VideoWriter_fourcc(*'MP4V')
# w= int(p1.get(3))
# h =int(p1.get(4))
# p2=cv2.VideoWriter("images/2.mp4", f, int(p1.get(5)), (w,h))
# i=0
# while p1.isOpened()==True:
# 	ret, m1=p1.read()
# 	if ret==True:
# 		#只錄一小段，算秒數做區隔
# 		i+=1
# 		# if i>90 and i<=200:
# 		p2.write(m1)
# 		print("當前影格:", p1.get(1))
# 		cv2.imshow("Image 1", m1)
# 		#當程式執行不等於-1時，會關閉程式
# 		if cv2.waitKey(33)!=-1:
# 			break
# 	else:
# 		break
# p2.release()
# cv2.destroyAllWindows()

#圖形
m1=np.full((150, 300, 3), (100, 200, 255), np.uint8)
# cv2.line(m1, (10,10), (100, 10), (255, 255, 255), 2)
# cv2.rectangle(m1, (1,15), (100, 80), (255, 255, 255), -1)
# cv2.circle(m1, (150, 100), 50, (250,0, 0), -1)
# cv2.imshow("Image 1", m1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#文字
from PIL import ImageFont, ImageDraw, Image
# m1=Image.fromarray(m1)

# f= ImageFont.truetype("images/msjh.ttc",30)
# ImageDraw.Draw(m1).text((10, 10), "這是說謊的味道", (255, 0, 0), f)
# m1= np.array(m1)
m1= cv2.imread("images/10.jpg", 1)
# m2= np.full(m1.shape, 2, np.uint8)
# # m3 =cv2.add(m1, m2)
# # m3=cv2.subtract(m1, m2)
# # m3=cv2.absdiff(m1, m2)
# # m3=cv2.divide(m1, m2)
# m3=cv2.multiply(m1, m2)
# w = 300
# h = int((w/m1.shape[1]*m1.shape[0]))
# h = 300
# w = int((h/m1.shape[0]*m1.shape[1]))
# m2=cv2.resize(m1, (w, h))
# m2=cv2.flip(m1, -1)
# d=cv2.getRotationMatrix2D((300, 300), 45, 1)
# m2=cv2.warpAffine(m1, d, (600,600))
# m2=np.full(m1.shape, 255, np.uint8)
# m2[325:500,100:250] = m1[325:500,100:250]
# m2[325:500] = m1[325:500]
# m2[:,325:500] = m1[:,325:500]
m1[50:250,100:250]=255


cv2.imshow("Image 1", m1)
# cv2.imshow("Image 1", m2)
# cv2.imshow("Image 1", m3)
cv2.waitKey(0)
cv2.destroyAllWindows()

