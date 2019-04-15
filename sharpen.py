import cv2
import numpy as np 
from matplotlib import pyplot as plt 

img = cv2.imread('laplacian1.jpg')

kernel = np.matrix('0 0 0; 0 2 0; 0 0 0')

enh = cv2.filter2D(img , -1, kernel);
blur1 = cv2.blur(img, (3,3))
blur2 = cv2.GaussianBlur(img, (11,11), 0)

diff1 = abs(img - blur1)
diff2 = abs(img - blur2)
diff3 = abs(enh - blur1)

plt.subplot(331), plt.imshow(img, cmap = 'gray'),plt.title('original'),plt.axis('off')
plt.subplot(332), plt.imshow(blur1, cmap = 'gray'),plt.title('uniform blur'),plt.axis('off')
plt.subplot(333), plt.imshow(diff1, cmap = 'gray'),plt.title('difference'),plt.axis('off')
plt.subplot(334), plt.imshow(img, cmap = 'gray'),plt.title('original'),plt.axis('off')
plt.subplot(335), plt.imshow(blur2, cmap = 'gray'),plt.title('Gaussian blur'),plt.axis('off')
plt.subplot(336), plt.imshow(diff2, cmap = 'gray'),plt.title('difference'),plt.axis('off')
plt.subplot(337), plt.imshow(enh, cmap = 'gray'),plt.title('enhanced'),plt.axis('off')
plt.subplot(338), plt.imshow(blur1, cmap = 'gray'),plt.title('uniform blur'),plt.axis('off')
plt.subplot(339), plt.imshow(diff3, cmap = 'gray'),plt.title('sharpened'),plt.axis('off')

plt.show()