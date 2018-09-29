import cv2
from collections import deque
from imutils.video import VideoStream
import imutils
import winsound
import time
import numpy as np 
import pyautogui
import screeninfo
#from playsound import playsound
#import wave
#from pygame import mixer
#import vlc
#import pyglet
pts=deque(maxlen=45	)
screen = screeninfo.get_monitors()[0]
cap=cv2.VideoCapture(0)
counter = 0
mouse = 0
p=-1
s=0
a=0
b=0
c=0
d=0
a1=0
b1=0
c1=0
d1=0
g=0
dynamic_square=0
delta_x= 20
delta_y = 20
dynamic_bool = 0
x_prev = 0
y_prev =0
pyautogui.FAILSAFE = False

while(1):
	_,img=cap.read()
	img2 = img.copy()
	hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

	img2 = imutils.resize(img2, width=600)
	img2 = cv2.GaussianBlur(img2, (11, 11), 0)

	red_lower=np.array([0,200,100],np.uint8) #136,87,111 -- 7,255,255
	red_upper=np.array([10,255,255],np.uint8)
	
	blue_lower=np.array([100,120,80],np.uint8)
	blue_upper=np.array([120,180,150],np.uint8)


	yellow_lower=np.array([20,155,180],np.uint8)
	yellow_upper=np.array([30,255,255],np.uint8)

	green_lower=np.array([60,100,50],np.uint8) #50.150.60 ->85.255.200 === 30,100,50 74,255,255
	green_upper=np.array([90,255,255],np.uint8)

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

	# green=cv2.dilate(green,kernal)
	# res3=cv2.bitwise_and(img,img,mask=green)

	green = cv2.erode(green, None, iterations = 2)
	green=cv2.dilate(green, None, iterations = 2)

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
	area_green=0	


	(_,contours,hierarchy)=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	for pic,contour in enumerate(contours):
		area=cv2.contourArea(contour)
		if(area>300):
			x,y,w,h=cv2.boundingRect(contour)
			img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
			cv2.putText(img,"RED",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255))


	(_,contours,hierarchy)=cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)	



	for pic,contour in enumerate(contours):
		area=cv2.contourArea(contour)
		if(area>300):
			x1,y1,w1,h1=cv2.boundingRect(contour)
			img=cv2.rectangle(img,(x1,y1),(x1+w1,y1+h1),(255,0,0),2)
			cv2.putText(img,"BLUE",(x1,y1),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,0,0))


	(_,contours,hierarchy)=cv2.findContours(yellow,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	for pic,contour in enumerate(contours):
		area=cv2.contourArea(contour)
		if(area>300):
			x2,y2,w2,h2=cv2.boundingRect(contour)
			img=cv2.rectangle(img,(x2,y2),(x2+w2,y2+h2),(0,255,255),2)
			cv2.putText(img,"YELLOW",(x2,y2),cv2.FONT_HERSHEY_SIMPLEX,1.0,(0,255,255))		

	(_,contours,hierarchy)=cv2.findContours(green,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	for pic,contour in enumerate(contours):
		area=cv2.contourArea(contour)
		area_green =area
		if(area>300):
			x3,y3,w3,h3=cv2.boundingRect(contour)
			img=cv2.rectangle(img,(x3,y3),(x3+w3,y3+h3),(0,255,0),2)
			cv2.putText(img,"GREEN",(x3,y3),cv2.FONT_HERSHEY_SIMPLEX,1.0,(0,255,0))

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




	# j=0

	# if((x1<max(x3,x3+w3)and x1>min(x3,x3+w3)) and (y1<max(y3,y3+h3) and y1>min(y3,y3+h3))):
	# 	j+=1
	# elif((x1<max(x3,x3+w3)and x1>min(x3,x3+w3)) and (y1+h1<max(y3,y3+h3) and y1+h1>min(y3,y3+h3))):
	# 	j+=1	
	# elif((x1+w1<max(x3,x3+w3) and x1+w1>min(x3,x3+w3)) and (y1<max(y3,y3+h3) and y1>min(y3,y3+h3))):
	# 	j+=1
	# elif((x1+w1<max(x3,x3+w3) and x1+w1>min(x3,x3+w3)) and (y1+h1<max(y3,y3+h3) and y1+h1>min(y3,y3+h3))):
	# 	j+=1

	# if((x<max(x2,x2+w2) and x>min(x2,x2+w2)) and (y<max(y2,y2+h2) and y>min(y2,y2+h2))):
	# 	j+=1
	# elif((x<max(x2,x2+w2) and x>min(x2,x2+w2)) and (y+h<max(y2,y2+h2) and y+h>min(y2,y2+h2))):
	# 	j+=1
	# elif((x+w<max(x2,x2+w2) and x+w>=min(x2,x2+w2)) and (y<max(y2,y2+h2) and y>min(y2,y2+h2))):
	# 	j+=1
	# elif((x+w<max(x2,x2+w2)&x+w>min(x2,x2+w2)) and (y+h<max(y2,y2+h2) and y+h>min(y2,y2+h2))):
	# 	j+=1

	# if(j>=2):
	# 	pyautogui.FAILSAFE+=(p)
	# 	p*=(-1)
	
	i=0

	if((x<max(x1,x1+w1) and x>min(x1,x1+w1)) and (y<max(y1,y1+h1) and y>min(y1,y1+h1))):
		i+=1
	elif((x<max(x1,x1+w1) and x>min(x1,x1+w1)) and (y+h<max(y1,y1+h1) and y+h>min(y1,y1+h1))):
		i+=1
	elif((x+w<max(x1,x1+w1) and x+w>=min(x1,x1+w1)) and (y<max(y1,y1+h1) and y>min(y1,y1+h1))):
		i+=1
	elif((x+w<max(x1,x1+w1)&x+w>min(x1,x1+w1)) and (y+h<max(y1,y1+h1) and y+h>min(y1,y1+h1))):
		i+=1

	if(i>=1):
		pyautogui.click()
		winsound.Beep(12000,400)

	if((x2<max(x3,x3+w3) and x2>min(x3,x3+w3)) and (y2<max(y3,y3+h3) and y2>min(y3,y3+h3))):
		g+=1
	elif((x2<max(x3,x3+w3) and x2>min(x3,x3+w3)) and (y2+h2<max(y3,y3+h3) and y2+h2>min(y3,y3+h3))):
		g+=1
	elif((x2+w2<max(x3,x3+w3) and x2+w2>=min(x3,x3+w3)) and (y2<max(y3,y3+h3) and y2>min(y3,y3+h3))):
		g+=1
	elif((x2+w2<max(x3,x3+w3) and x2+w2>min(x3,x3+w3)) and (y2+h2<max(y3,y3+h3) and y2+h2>min(y3,y3+h3))):
		g+=1

	if(g>=5):
		pyautogui.click(button = 'right')
		winsound.Beep(18000,400)
		g=0

	if((x2==0 and y2==0)and (x3==0 and y3==0)):
		a=0
		a1=0
	if((x2==0 and y2==0)and(x3!=0 and y3!=0)):
		a+=1

	if(a>=8 and a<=60):
		if((x3==0 and y3==0)and(x2!=0 and y2!=0)):
			a1+=1

	if(a1<=60 and a1>=8):
		print('first working')
		#im1 = pyautogui.screenshot()
		#im2 = pyautogui.screenshot('my_screenshot.png')
		winsound.Beep(4000,800)
		a=0
		a1=0

	if((x==0 and y==0)and (x1==0 and y1==0)):
		b=0
		b1=0
	if((x==0 and y==0)and(x1!=0 and y1!=0)):
		b+=1

	if(b>=8 and b<=60):
		if((x1==0 and y1==0)and(x!=0 and y!=0)):
			b1+=1

	if(b1<=60 and b1>=8):
		print('second working')
		#winsound.Beep(4000,800)
		#playsound('C:\Users\dell\Downloads\PartyRockAnthem.mp3')
		#wave=open("C:\Users\dell\Downloads\PartyRockAnthem.mp3"."r")
		#mixer.init()
		#mixer.music.load('C:\Users\dell\Downloads\PartyRockAnthem.mp3')
		#mixer.music.play()

		b=0
		b1=0
#THird STATIC gesture --->creating tons of errors
	# if((x3==0 and y3==0)and (x1==0 and y1==0)):
	# 	c=0
	# 	c1=0
	# if((x3==0 and y3==0)and(x1!=0 and y1!=0)):
	# 	c+=1
	# if(c>=8 and c<=60):
	# 	if((x1==0 and y1==0)and(x3!=0 and y3!=0)):
	# 		c1+=1

	# if(c1<=60 and c1>=8):
	# 	print('third working')
	# 	winsound.Beep(4000,800)
	# 	c=0
	# 	c1=0

	if((x2==0 and y2==0)and (x==0 and y==0)):
		d=0
		d1=0
	if((x2==0 and y2==0)and(x!=0 and y!=0)):
		d+=1

	if(d>=8 and d<=60):
		if((x==0 and y==0)and(x2!=0 and y2!=0)):
			d1+=1

	if(d1<=60 and d1>=8):
		print('third working')
		#music=pyglet.media.load('PartyRockAnthem.mp3',streaming=False)
		#pyglet.app.run()

		winsound.Beep(4000,800)
		d=0
		d1=0


	#print(screen.width)
	if((abs(x-x_prev) > 2 or abs(y - y_prev) > 2) and (x!=0 or y!=0)):
		x_prev = x
		y_prev = y
		pyautogui.moveTo(x_prev* (60+screen.width)/640, y_prev*(40 + screen.height)/480,0.1,pyautogui.easeInOutQuad)
	else:
		pyautogui.moveTo(x_prev*(60+screen.width)/640, y_prev*(40 + screen.height)/480,0.1,pyautogui.easeInOutQuad)

	if(s==10):
		#time.sleep(2)
		winsound.Beep(2500,800)

		cv2.imwrite("ITSP" + str(counter)+ ".png",img)
		s=0

	if(s>=1):
		s+=1
	if(k>=2):
		winsound.Beep(2000,200)
		time.sleep(2)
		s+=1
		counter += 1
		k=0

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

		# if radius > 10:
		# 	cv2.circle(img, (int(xc), int(yc)), int(radius),(0, 255, 255), 2)
		# 	cv2.circle(img, center, 5, (0, 0, 255), -1)
	dynamic_square=0
	for i in range(1, len(pts)):
		# if either of the tracked points are None, ignore
		# them
		if pts[i - 1] is None or pts[i] is None:
			continue
		#print("i : ", i)

		# otherwise, compute the thickness of the line and
		# draw the connecting lines
		#cv2.line(img, pts[i - 1], pts[i], (255, 0, 255), 1)
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

	# print(dynamic_square)
	cv2.namedWindow("colour tracking",cv2.WINDOW_NORMAL)       
	cv2.moveWindow("colour tracking", screen.x - 1, screen.y - 1)
	cv2.resizeWindow("colour tracking",screen.width,screen.height)
	cv2.imshow("colour tracking",img)
	if cv2.waitKey(10) & 0xff == ord('q')	:
	    cap.release()
	    cv2.destroyAllWindows()
	    break 