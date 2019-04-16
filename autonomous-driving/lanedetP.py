import cv2 as cv
import numpy as np

img = cv.imread('lane.jpg')
img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

lower = np.array([40, 8, 80])   #decreased hue
upper = np.array([80, 28, 200])     #first tweaked the value - increased
mask = cv.inRange(img_hsv, lower, upper)
kernel = np.ones([5, 5])
mask = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)

cv.imshow("mask for lane", mask)
cv.waitKey(0)

edges = cv.Canny(mask, 75, 150)
cv.imshow("edges", edges)
cv.waitKey(0)

lines = cv.HoughLinesP(edges, 1, np.pi/180, 100, maxLineGap = 200)     
#print(lines)

if(lines.any()):
	for line in lines:
		x1, y1, x2, y2 = line[0]
		cv.line(img, (x1, y1), (x2, y2), [0, 0, 255], 2)  #does this funtion return a value or not?

cv.imshow('linesdetected', img)
cv.waitKey(0)
cv.destroyAllWindows()