import cv2
import cvzone

thres=0.6
nmsThres=0.2

cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

classs=[]
classfile='classsco.names'
with open(classfile,'rt') as f:
  classs=f.read().split('\n')

#print(classs)

configpath='ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightspath="frozen_inference_graph.pb"

net = cv2.dnn_DetectionModel(weightspath,configpath)
net.setInputSize(3230,320)
net.setInputScale(1.0/127.5)
net.setInputMean((127.5,127.5,127.5))
net.setInputSwapRB(True)

#while True:
for i in range(1):
  sucess, img= cap.read()
  #img=cv2.imread("/content/img.jpg")
  classIds,confs,bbox=net.detect(img,confThreshold=thres,nmsThreshold=nmsThres)
  try:
    for classId, conf, box in zip(classIds.flatten(),confs.flatten(),bbox):
      cvzone.cornerRect(img,box,rt=1)
      print(classId,conf,bbox)
      cv2.putText(img,f'{classs[ClassId-1].upper()}{round(conf*100,2)}',
                  (box[0]+10,box[1]+30),cv2.FONT_HERSHEY_COMPLEX_SMALL,
                  1,(0,255,0),2)

  except:
    pass
  

  cv2.imshow("image",img)
  cv2.waitKey(1)
