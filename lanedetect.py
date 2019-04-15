import cv2 as cv
import numpy as np

img = cv.imread('lane.jpg')
img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

lower = np.array([40, 8, 80])   #decreased hue
upper = np.array([80, 28, 200])     #first tweaked the value - increased
mask = cv.inRange(img_hsv, lower, upper)
kernel = np.ones([3,3])
mask = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)

cv.imshow("mask for lane", mask)
cv.waitKey(0)

edges = cv.Canny(mask, 75, 150)
cv.imshow("edges", edges)
cv.waitKey(0)

lines = cv.HoughLines(edges, 1, np.pi/180, 100)     #last argument is the no. of votes. Try tweaking.

if(lines.any()):
	for line in lines:
		r, theta = line[0]
		a = np.cos(theta)     #possible radian degree issue?
		b = np.sin(theta)
		x0 = a*r
		y0 = b*r
		x1 = int(x0 - 1000*(-b))
		y1 = int(y0 - 1000*a)
		x2 = int(x0 + 1000*(-b))
		y2 = int(y0 + 1000*a)

		cv.line(img, (x1, y1), (x2, y2), [0, 0, 255], 2)  #does this funtion return a value or not?

cv.imshow('linesdetected', img)
cv.waitKey(0)
cv.destroyAllWindows()