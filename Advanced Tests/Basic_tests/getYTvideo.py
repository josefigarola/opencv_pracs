#pip install pafy
#sudo pip install --upgrade youtube_dl

import cv2 as cv
import pafy

url   = "https://www.youtube.com/watch?v=icPHcK_cCF4"
video = pafy.new(url)
best  = video.getbest(preftype="webm")
#documentation: https://pypi.org/project/pafy/

capture = cv.VideoCapture(best.url)
check, frame = capture.read()
print (check, frame)

cv.imshow('frame',frame)
cv.waitKey(0)

capture.release()
cv.destroyAllWindows()