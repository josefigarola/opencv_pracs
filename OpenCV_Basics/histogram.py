import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('photos/ny.jpg')
cv.imshow('NY',img)

blank = np.zeros(img.shape[:2], dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

circle_mask = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 100, 255, -1)

masked = cv.bitwise_and(img, img, mask=circle_mask)
cv.imshow('Masked Image',circle_mask)

# Histogram
# CalcHist function allows you to see the distribution of pixels 
# The peaks shows us the intensity of the pixels
# Images -> List of the images to compute
# Channels -> Index of the channel we want to compute a histogram for
# Maks -> Specific portion of an image?
# histSize -> Number of BINS for computing a histogram
# Range -> All posible pixel values

# Grayscale histogram
gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('Number of Pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()
 
# Colour Histogram
colors = ('b','g','r')

plt.figure()
plt.title('Colour Histogram')
plt.xlabel('Bins')
plt.ylabel('Number of Pixels')

for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], circle_mask, [256], [0,256])
    plt.plot(hist, color=col) 
    plt.xlim([0,256])  

plt.show()

cv.waitKey(0)