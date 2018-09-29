from collections import deque
from imutils.video import VideoStream
import imutils
import time
import argparse
import cv2
import time
import numpy as np 
import pyautogui
import math
import screeninfo
""" 
	edited by yash on 13/6 4:54
"""
pts=deque(maxlen=64	)
screen = screeninfo.get_monitors()[0]
# for full screen implementation
cap=cv2.VideoCapture(0)

counter = 0
pyautogui.FAILSAFE = False
x3_prev = 0
y3_prev = 0
w3_prev = 0
h3_prev = 0
dynamic_square=0
delta_x= 20
delta_y = 20
dynamic_bool = 0
print("program started")

red_lower=np.array([0,200,60],np.uint8) #136,87,111 -- 7,255,255// 0,200,100
red_upper=np.array([10,200,100],np.uint8)

blue_lower=np.array([110,200,80],np.uint8)
blue_upper=np.array([130,255,130],np.uint8)

yellow_lower=np.array([20,155,180],np.uint8)
yellow_upper=np.array([30,255,255],np.uint8)

green_lower=np.array([30,100,50],np.uint8) # 50 150 60 --> 80 255 200
green_upper=np.array([74,255,255],np.uint8)

m_lower = math.tan(math.degrees(0))
m_upper = math.tan(math.degrees(85))

_,img=cap.read()

hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
green=cv2.inRange(hsv,green_lower,green_upper)
kernal=np.ones((5,5),"uint8")

(_,contours,hierarchy)=cv2.findContours(green,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for pic,contour in enumerate(contours):
	area=cv2.contourArea(contour)
	if(area>300):
		x3_prev,y3_prev,w3_prev,h3_prev=cv2.boundingRect(contour)
		img=cv2.rectangle(img,(x3_prev,y3_prev),(x3_prev+w3_prev,y3_prev+h3_prev),(0,255,255),2)
		cv2.putText(img,"GREEN",(x3_prev,y3_prev),cv2.FONT_HERSHEY_SIMPLEX,1.0,(0,255,0))

m_counter = 0
randomizer = 0


while(1):
	_,img=cap.read()
	#img = vs.read()
	randomizer +=1
	img = imutils.resize(img, width=600)
	img = cv2.GaussianBlur(img, (11, 11), 0)

	hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

	red=cv2.inRange(hsv,red_lower,red_upper)
	blue=cv2.inRange(hsv,blue_lower,blue_upper)
	yellow=cv2.inRange(hsv,yellow_lower,yellow_upper)
	green=cv2.inRange(hsv,green_lower,green_upper)

	kernal=np.ones((5,5),"uint8")

	red=cv2.dilate(red,kernal)
	res=cv2.bitwise_and(img,img,mask=red)

	blue=cv2.dilate(blue,kernal)
	res1=cv2.bitwise_and(img,img,mask=blue)

	yellow=cv2.dilate(yellow,kernal)
	res2=cv2.bitwise_and(img,img,mask=yellow)

	green = cv2.erode(green, None, iterations = 2)
	green=cv2.dilate(green, None, iterations = 2)
	#res3=cv2.bitwise_and(img,img,mask=green)

	x=0
	x1=0
	x2=0
	x3=0
	y=0
	y1=0
	y2=0
	y3=0
	h=0
	h1=0
	h2=0
	h3=0
	w1=0
	w=0
	w2=0
	w3=0	
	area_red = 0
	area_green = 0

	(_,contours,hierarchy)=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	for pic,contour in enumerate(contours):
		area=cv2.contourArea(contour)
		area_red = area
		if(area>300):
			x,y,w,h=cv2.boundingRect(contour)
			#BOX AROUND RED!!!!!!!
			img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
			cv2.putText(img,"RED",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255))


	(_,contours,hierarchy)=cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)	

	for pic,contour in enumerate(contours):
		area=cv2.contourArea(contour)
		if(area>300):
			x1,y1,w1,h1=cv2.boundingRect(contour)
			img=cv2.rectangle(img,(x1,y1),(x1+w1,y1+h1),(0,0,0),2)
			cv2.putText(img,"BLUE",(x1,y1),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,0,0))


	(_,contours,hierarchy)=cv2.findContours(yellow,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	for pic,contour in enumerate(contours):
		area=cv2.contourArea(contour)
		if(area>300):
			x2,y2,w2,h2=cv2.boundingRect(contour)
			img=cv2.rectangle(img,(x2,y2),(x2+w2,y2+h2),(0,255,255),2)
			cv2.putText(img,"YELLOW",(x2,y2),cv2.FONT_HERSHEY_SIMPLEX,1.0,(0,255,0))		

	(_,contours,hierarchy)=cv2.findContours(green,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	for pic,contour in enumerate(contours):
		area=cv2.contourArea(contour)
		area_green = area
		# if(area>300):
		# 	x3,y3,w3,h3=cv2.boundingRect(contour)
		# 	img=cv2.rectangle(img,(x3,y3),(x3+w3,y3+h3),(0,255,255),2)
		# 	cv2.putText(img,"GREEN",(x3,y3),cv2.FONT_HERSHEY_SIMPLEX,1.0,(0,255,0))

	k=0

	if((x1<max(x2,x2+w2)and x1>min(x2,x2+w2))and(y1<max(y2,y2+h2)and y1>min(y2,y2+h2))):
		k+=1
	elif((x1<max(x2,x2+w2)and x1>min(x2,x2+w2))and(y1+h1<max(y2,y2+h2)and y1+w1>min(y2,y2+h2))):
		k+=1	
	elif((x1+w1<max(x2,x2+w2)and x1+w1>min(x2,x2+w2))and(y1<max(y2,y2+h2)and y1>min(y2,y2+h2))):
		k+=1
	elif((x1+w1<max(x2,x2+w2)and x1+w1>min(x2,x2+w2))and(y1+h1<max(y2,y2+h2)and y1+h1>min(y2,y2+h2))):
		k+=1

	if((x<max(x3,x3+w3)and x>min(x3,x3+w3))and(y<max(y3,y3+h3)and y>min(y3,y3+h3))):
		k+=1
	elif((x<max(x3,x3+w3)and x>min(x3,x3+w3))and(y+h<max(y3,y3+h3)and y+h>min(y3,y3+h3))):
		k+=1
	elif((x+w<max(x3,x3+w3)and x+w>min(x3,x3+w3))and(y<max(y3,y3+h3)and y>min(y3,y3+h3))):
		k+=1
	elif((x+w<max(x3,x3+w3)and x+w>min(x3,x3+w3))and(y+h<max(y3,y3+h3)and y+h>min(y3,y3+h3))):
		k+=1

	h4=min(x,x3,x+h,x3+h3)-max(x1,x2,x1+h1,x2+h2)
	w4=min(y,y3,y+w,y3+w3)-max(y1,y2,y1+w1,y2+w2)
	#pyautogui.moveTo(x3* 1920/640, y3*1080/480)

	
	if(k>=2):
		time.sleep(4)
		#crop=img[y:y2,x:x2]
		cv2.imwrite("ITSP" + str(counter)+ ".png",crop)
		counter += 1
		k=0

	if (randomizer %5 == 0):
		if (x3 != x3_prev):
			m_current = (y3 - y3_prev)/(x3 - x3_prev)
		else :
			m_current = 0
		if (m_current < m_upper and m_current > m_lower):
			m_counter +=1
		else :
			m_counter = 0

		if (m_counter > 2) :
			m_counter = 0
			print ("gesture working")

		if (m_counter !=0):
			print ( m_counter)

		#print(x3,y3,m_current,x3_prev,y3_prev)

		x3_prev = x3
		y3_prev = y3 

	""" 
	edited by yash jain 13/6 4:54
	"""
	# find contours in the mask and initialize the current
	# (x, y) center of the ball
	cnts = cv2.findContours(green.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	cnts = cnts[1] 
	#image, contours, hierarchy = cv2.findContours(im_bw.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	#if imutils.is_cv2() else cnts[1]
	center = None
	if (len(cnts)>0 and area_green > 300):
		c = max(cnts, key=cv2.contourArea)
		((xc, yc), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		if (M["m00"]!=0):
			center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
			pts.appendleft(center)
			dynamic_bool =0

		if radius > 10:
			# draw the circle and centroid on the frame,
			# then update the list of tracked points
			cv2.circle(img, (int(xc), int(yc)), int(radius),(0, 255, 255), 2)
			cv2.circle(img, center, 5, (0, 0, 255), -1)
		# loop over the set of tracked points
	dynamic_square=0
	for i in range(1, len(pts)):
		# if either of the tracked points are None, ignore
		# them
		if pts[i - 1] is None or pts[i] is None:
			continue
		#print("i : ", i)

		# otherwise, compute the thickness of the line and
		# draw the connecting lines
		cv2.line(img, pts[i - 1], pts[i], (255, 0, 255), 1)
		if (i>2 and abs(pts[i][0] - pts[i-1][0]) <= delta_x and abs(pts[i][1] - pts[i-1][1]) >=3 and dynamic_bool == 0):
			dynamic_square +=1
		elif(i > 2 and abs(pts[i][1] - pts[i-1][1]) <= delta_y and abs(pts[i][0] - pts[i-1][0]) >= 3 and dynamic_bool ==0):
			dynamic_square +=1
		else:
			dynamic_square =0
		if dynamic_square > 25:
		 	print("dynamic gesture", dynamic_square)
		 	pts.clear()
		 	dynamic_square = 0
		 	dynamic_bool =1
		 	break

	print(dynamic_square)
	cv2.namedWindow("colour tracking",cv2.WINDOW_NORMAL)       
	cv2.moveWindow("colour tracking", screen.x - 1, screen.y - 1)
	cv2.resizeWindow("colour tracking",screen.width,screen.height)
	#for full screen resizing!!
	cv2.imshow("colour tracking",img)
	if cv2.waitKey(10) & 0xff == ord('q')	:
	    cap.release()
	    cv2.destroyAllWindows()
	    break 







