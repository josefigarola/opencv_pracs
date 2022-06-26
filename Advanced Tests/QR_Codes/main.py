import cv2 as cv
import numpy as np


def show_qr_detection(img, pts):
    """Draws both the lines and corners based on the array of vertices of the found QR code"""

    pts = np.int32(pts).reshape(-1, 2)

    for j in range(pts.shape[0]):
        cv.line(img, tuple(pts[j]), tuple(pts[(j + 1) % pts.shape[0]]), (255, 0, 0), 5)

    for j in range(pts.shape[0]):
        cv.circle(img, tuple(pts[j]), 10, (255, 0, 255), -1)

    return img

image = cv.imread("Computer_Vision\Tests\QR_Codes\Photos\Mochomos.png")
qr_code_detector = cv.QRCodeDetector()
data, bbox, rectified_qr_code = qr_code_detector.detectAndDecode(image)

cv.imshow("Original", image)

if len(data) > 0:
    try:
        print("Decoded Data : {}".format(data))
        qr = show_qr_detection(image, bbox)
    except:
        print("Error")

cv.waitKey(0)
cv.destroyAllWindows()