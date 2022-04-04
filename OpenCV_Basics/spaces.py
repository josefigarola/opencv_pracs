import cv2 as cv
import matplotlib.pyplot as plt

# matplot uses RGB colors therefore when displaying an image you can see the colors inverted,
# whilst opencv uses BGR colors

img = cv.imread('photos/gas_cara.jpg.crdownload')
cv.imshow('Gas',img)

""" plt.imshow(img)
plt.show() """

# BGR --> Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)

# BGR --> HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('HSV',hsv)

# BGR --> LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
# cv.imshow('LAB',lab)

# BGR --> RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)
# plt.imshow(rgb)
# plt.show()

""" INVERTED METHOD """
# HSV -> BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV to BGR',hsv_bgr)

# LAB -> BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_Lab2BGR)
cv.imshow('Lab to BGR',lab_bgr)

cv.waitKey(0)