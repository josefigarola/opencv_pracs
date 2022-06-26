''' This code implements the Harris corner detector. '''
import cv2 as cv

def HarrisDetector(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Get Harris corners
    # ksize must be between 3 and 31
    # If higher the ksize, more likely to detect intersections
    dst = cv.cornerHarris(gray, 2, 31, 0.04) # Parameters: image, blockSize, ksize, k

    # Color Harry corners over image
    img[dst > 0.01 * dst.max()] = [0, 0, 255]

    # Show image
    cv.imshow("Harris Corners", img)

if __name__ == '__main__':

    # Read and Grayscale image
    img = cv.imread("Computer_Vision\Tests\DetectingFeatures\Photos\Chess_board.png")

    HarrisDetector(img=img)

    cv.waitKey(0)
    cv.destroyAllWindows()