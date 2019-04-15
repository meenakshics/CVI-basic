import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
	
	ret, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lower = np.array([29, 86, 6])
	upper = np.array([100, 255, 255])
	mask = cv2.inRange(hsv, lower, upper)
	
	kernel = np.ones((5,5))
	#mask = cv2.erode(mask, kernel, iterations = 1)
	#mask = cv2.dilate(mask, kernel, iterations = 1)
	mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

	cnt = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2] #-2 means second from the end. This function returns multiple values.

	if cnt:
		cMax = max(cnt, key = cv2.contourArea)
		(x, y), radius = cv2.minEnclosingCircle(cMax)
		centre = (int(x), int(y))
		radius = int(radius)
		cv2.circle(frame, centre, radius, (255, 255, 255), 2)
		
		#x1, y1, w, h = cv2.boundingRect(cMax)
		#cv2.rectangle(frame, (x1, y1), (x1+w, y1+h), (255, 255, 255), 2)

	cv2.imshow('frame', frame)
	cv2.imshow('mask', mask)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()