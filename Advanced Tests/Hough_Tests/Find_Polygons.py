from cv2 import COLOR_BGR2GRAY
import numpy as np
import cv2 as cv

# Reading image
img = cv.imread('Computer_Vision\Tests\Hough_Tests\photos\poligonos.png')
cv.imshow('Image',img)

# Reading same image in another variable and
# converting to gray scale.
gray = cv.cvtColor(img, COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# Converting image to a binary image
# (black and white only image).
_,threshold = cv.threshold(gray, 110, 255,
							cv.THRESH_BINARY)

# Detecting shapes in image by selecting region
# with same colors or intensity.
contours,_=cv.findContours(threshold, cv.RETR_TREE,
							cv.CHAIN_APPROX_SIMPLE)

# Searching through every region selected to
# find the required polygon.
for cnt in contours :
	area = cv.contourArea(cnt)

	# Shortlisting the regions based on there area.
	if area > 400:
		approx = cv.approxPolyDP(cnt,
								0.009 * cv.arcLength(cnt, True), True)
		print(approx)

		# Checking if the no. of sides of the selected region is 7.
		if(len(approx) > 4):
			cv.drawContours(img, [approx], 0, (0, 0, 0), 3)

# Showing the image along with outlined arrow.
cv.imshow('Outlined', img)

# Exiting the window if 'q' is pressed on the keyboard.
if cv.waitKey(0) & 0xFF == ord('q'):
	cv.destroyAllWindows()
