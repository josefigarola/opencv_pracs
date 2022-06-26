import color_mask_seg as cm
import contuours_seg as cnt
import thresh_seg as tseg
import kmeans_seg as kmeans
import watershed_seg as water
import cv2 as cv

# img = cv.imread('Computer_Vision\Tests\Segmentation_tests\photos\semaforo2.jpg')
# cv.imshow('Image',img)

# kmeans.K_means(img=img, Kvalue=16)
# cnt.cnt_seg(img=img)
# tseg.thresh_seg(img=img)
# cm.color_mask_seg(img=img)

cam = cv.VideoCapture(0)

while True:
    check, frame = cam.read()
    #kmeans.K_means(img=frame, Kvalue=4)
    #cnt.cnt_seg(img=frame)
    cm.color_mask_seg(img=frame)

    ''' Close Windows '''
    key = cv.waitKey(1)
    # If Esc key pressed break the process
    if key == 27:
        break

cam.release()
cv.destroyAllWindows()