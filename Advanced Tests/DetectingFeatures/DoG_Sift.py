''' 
This code compute SIFT algorithm to detect features 
SIFT will not output different results depending on the scale of the image 
SIFT does not detect keypoints (which is done with the Difference of Gaussians (DoG); 
instead, it describes the region surrounding them by means of a feature vector.
'''
import cv2 as cv

def SiftFeatures(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Compute the features and descriptors of the grayscale image
    sift = cv.xfeatures2d.SIFT_create()
    keypoints, descriptors = sift.detectAndCompute(gray, None)

    # cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINT 
    # In order to draw a visualization of the scale and orientation of each keypoint.
    cv.drawKeypoints(img, keypoints, img, (255, 0, 255))

    cv.imshow("SIFT", img)

if __name__ == '__main__':

    img = cv.imread('Computer_Vision\Tests\DetectingFeatures\Photos\Varese.jpg')

    # Resize image
    img = cv.resize(img, (600, 480), cv.INTER_AREA)

    SiftFeatures(img=img)

    cv.waitKey(0)
    cv.destroyAllWindows()