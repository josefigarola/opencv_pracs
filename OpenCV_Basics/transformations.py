import cv2 as cv
import numpy as np

img = cv.imread('photos/cat.jfif')
cv.imshow('Cat',img)

# Translation (shiftin an image)
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0]) # (width,height)

    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated = translate(img, 100, 100) # Shift 100 pixels to the right and 100 Down
cv.imshow('Translated',translated)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -90)
cv.imshow('Rotated',rotated)

# Resezing
# Shrinking -> INTER_AREA
# Enlarging -> INTER_LINEAR or INTER_CUBIC
resized = cv.resize(img, (500,500), interpolation=cv.INTER_LINEAR)
cv.imshow('Resized',resized)

# Flipping
flip = cv.flip(img, -1) # 0 (vertically), 1(Horizontally) or -1 (Both)
cv.imshow('Flipped',flip)

cv.waitKey(0)