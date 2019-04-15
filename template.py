import cv2
import numpy as np

src = cv2.imread('ISpy.jpg', 1)
temp = cv2.imread('template.jpg', 1)

print 'Can you find the baseball?'
cv2.waitKey(3000)

cv2.imshow('Mess', src)
cv2.imshow('baseball', temp)
cv2.waitKey(0)
cv2.destroyAllWindows()

res = cv2.matchTemplate(src, temp, cv2.TM_SQDIFF_NORMED)
matchLoc = cv2.minMaxLoc(res)[-2]					 #maxLoc stores the value in (x,y) form.

h, w, channel = temp.shape
bot_rgt = (maxLoc[0] + w, maxLoc[1] + h)
cv2.rectangle(src, matchLoc, bot_rgt, (0,255,0), 2)  #maxLoc is upper left and bot_rgt is bottom right
cv2.imshow('found it!', src)
cv2.imshow('after matching', res)
cv2.waitKey(0)
cv2.destroyAllWindows()