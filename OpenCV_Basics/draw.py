""" This programm show different ways to draw on an image or on a blank image
change the figure's scale, colour, fonts.. """

import cv2 as cv
import numpy as np

# Create a blank image
blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)

# 1. Paint the image a certain colour (BGR colours)
""" blank[:] = 0,255,0 # Red image
cv.imshow('Green',blank)

blank[200:300, 300:400 ] = 255,0,0 # Add a blue square
cv.imshow('Square',blank) """

# 2. Draw a Rectangle
# Using rectangle method, it receives -> img, coordinate1, coordinate2, color, thickness
cv.rectangle(blank,(100,100),(250,250),(0,255,0),thickness=10) # To fill the rectangle use cv.FILLED or -1 in thickness attribute
# Another way to pass the coordinates attribute as fixed coordinates
cv.rectangle(blank,(100,100),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=10)
cv.imshow('Rectangle',blank)

# 3. Draw a circle
# Using Circle method, it receives -> img, coordinates of the center, radius, color, thickness
cv.circle(blank,(250,250),40,(0,0,255),thickness=-1)
cv.imshow('Circle',blank)

# 4. Draw a line
# Using Line method, it receives -> img, coordinate1, coordinate2, color, thickness
cv.line(blank,(250,250),(450,450),(255,0,0),thickness=3)
cv.imshow('Line',blank)

# 5. Write text on an image
# Using putText methos, it receives -> img, text, coordinates, font, font_size, color, thickness
cv.putText(blank,'Figarola',(50,450),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,255),thickness=2)
cv.imshow('Line',blank)

# Delay in ms for key to be pressed
cv.waitKey(5000)
# Close all windows opnened from opencv
cv.destroyAllWindows