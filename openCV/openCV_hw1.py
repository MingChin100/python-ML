import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

x = input("請輸入圖片檔名:")
y = input("請輸入浮水印內容:")
z = input("請輸入浮水印尺寸(px)：")
m1=cv2.imread("images/"+x, 1)
m1=Image.fromarray(m1)
f= ImageFont.truetype("images/msjh.ttc",int(z))
ImageDraw.Draw(m1).text((10, 10), str(y), (255, 0, 0), f)
m1= np.array(m1)
cv2.imshow("Image 1", m1)
cv2.waitKey(0)
cv2.destroyAllWindows()

