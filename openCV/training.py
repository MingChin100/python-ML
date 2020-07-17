import os
import cv2
import codecs
import sys

argv={}
for d in range(1,len(sys.argv)):
	d=d.split("=")
	argv[d[0]]=d[1]


SUCCESS_NAME="OK"
if 'WIDTH' in argv:
	SUCCESS_WIDTH=argv["WIDTH"]
else:
	SUCCESS_WIDTH=200

if 'HEIGHT' in argv:
	SUCCESS_HEIGHT=argv["HEIGHT"]
else:
	SUCCESS_HEIGHT=200

ERROR_NAME="NO"

if 'NUMSTAGES' in argv:
	NUMSTAGES=argv["NUMSTAGES"]
else:
	NUMSTAGES=5

if 'METHOD' in argv:
	METHOD=argv["METHOD"]
else:
	METHOD="LBP" #HAAR, LBP


OUT_TEXT=""
SUCCESS_NUM=0
for f in os.listdir(SUCCESS_NAME):
	NFL=SUCCESS_NAME+"/"+str("%05d"%(SUCCESS_NUM))+".png"
	os.rename(SUCCESS_NAME+"/"+f, NFL)
	img=cv2.imread(NFL)
	img=cv2.resize(img, (SUCCESS_WIDTH,SUCCESS_HEIGHT))
	cv2.imwrite(NFL,img)
	print(NFL)
	OUT_TEXT+=SUCCESS_NAME+"/"+f+" 1 0 0 "+str(img.shape[1])+" "+str(img.shape[0])+"\n"
	SUCCESS_NUM+=1

f=codecs.open(SUCCESS_NAME+".txt","w")
f.write(OUT_TEXT)
f.close()

OUT_TEXT=""
ERROR_NUM=0
for f in os.listdir(ERROR_NAME):
	NFL=ERROR_NAME+"/"+str("%05d"%(ERROR_NUM))+".png"
	os.rename(ERROR_NAME+"/"+f, NFL)
	print(NFL)
	OUT_TEXT+=NFL+"\n"
	ERROR_NUM+=1

f=codecs.open(ERROR_NAME+".txt","w")
f.write(OUT_TEXT)
f.close()
print("===opencv_createsamples===")
opencv_createsamples="opencv_createsamples.exe"
opencv_createsamples+=" -info "+SUCCESS_NAME+".txt -vec "+SUCCESS_NAME+".vec -bg "+ERROR_NAME+".txt -num "+str(SUCCESS_NUM)
opencv_createsamples+=" -w "+str(SUCCESS_WIDTH)+" -h "+str(SUCCESS_HEIGHT)
os.system(opencv_createsamples)

print("===opencv_traincascade===")
opencv_traincascade="opencv_traincascade.exe"
opencv_traincascade+=" -data xml/ -vec "+SUCCESS_NAME+".vec -bg "+ERROR_NAME+".txt -numPos "+str(SUCCESS_NUM)
opencv_traincascade+=" -numNeg "+str(ERROR_NUM)+" -numStages "+str(NUMSTAGES)
opencv_traincascade+=" -featureType "+METHOD
opencv_traincascade+=" -w "+str(SUCCESS_WIDTH)+" -h "+str(SUCCESS_HEIGHT)
opencv_traincascade+=" -precalcValBufSize 4048 -precalcIdxBufSize 4048 -numThreads 24 -maxFalseAlarmRate 0.5 -minHitRate 0.995"
os.system(opencv_traincascade)

