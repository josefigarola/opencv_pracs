#!/usr/bin/env python

from cv2 import VideoCapture, line
import matplotlib as plt
import numpy as np
import cv2 as cv
import os
import rospy
from std_msgs.msg import Float32

class Detect_Light:

    def __init__(self):
        self.__light = None

        #self.sub_vision_error = rospy.Subscriber(
        #    "/vision_error", Float32, self.img_feedback_callback
        #)

        #Checamos a cual publicar
        self.pub_light = rospy.Publisher("/cmd_vel", self.__light, queue_size=10)

        rospy.init_node("Traffic_Light", anonymous=True)
        self.rate = rospy.Rate(10)
        rospy.on_shutdown(self.stop)

    def stop(self): 
        self.pub_light.publish(0)

    def detect_semaforo(self,img):
        
        font = cv.FONT_HERSHEY_SIMPLEX
        cimg = img
        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

        # Color range Masks
        lower_red1 = np.array([0,100,100])
        upper_red1 = np.array([10,255,255])
        lower_red2 = np.array([160,100,100])
        upper_red2 = np.array([180,255,255])
        lower_green = np.array([40,50,50])
        upper_green = np.array([90,255,255])
        # lower_yellow = np.array([15,100,100])
        # upper_yellow = np.array([35,255,255])
        lower_yellow = np.array([15,150,150])
        upper_yellow = np.array([35,255,255])
        mask1 = cv.inRange(hsv, lower_red1, upper_red1)
        mask2 = cv.inRange(hsv, lower_red2, upper_red2)
        maskg = cv.inRange(hsv, lower_green, upper_green)
        masky = cv.inRange(hsv, lower_yellow, upper_yellow)
        maskr = cv.add(mask1, mask2)

        size = img.shape
    
        # Hough circle detect
        r_circles = cv.HoughCircles(maskr, cv.HOUGH_GRADIENT, 1, 80,
                                   param1=50, param2=10, minRadius=0, maxRadius=30)

        g_circles = cv.HoughCircles(maskg, cv.HOUGH_GRADIENT, 1, 60,
                                     param1=50, param2=10, minRadius=0, maxRadius=30)

        y_circles = cv.HoughCircles(masky, cv.HOUGH_GRADIENT, 1, 30,
                                     param1=50, param2=5, minRadius=0, maxRadius=30)

        # Traffic light detect per blob of the colors
        r = 5
        bound = 4.0 / 10
        if r_circles is not None:

            r_circles = np.uint16(np.around(r_circles))

            for i in r_circles[0, :]:
                if i[0] > size[1] or i[1] > size[0]or i[1] > size[0]*bound:
                    continue

                h, s = 0.0, 0.0
                for m in range(-r, r):
                    for n in range(-r, r):

                        if (i[1]+m) >= size[0] or (i[0]+n) >= size[1]:
                            continue
                        h += maskr[i[1]+m, i[0]+n]
                        s += 1
                if h / s > 50:
                    # Light is red, then stop
                    self.__light = 0

        if g_circles is not None:

            g_circles = np.uint16(np.around(g_circles))

            for i in g_circles[0, :]:
                if i[0] > size[1] or i[1] > size[0] or i[1] > size[0]*bound:
                    continue

                h, s = 0.0, 0.0
                for m in range(-r, r):
                    for n in range(-r, r):

                        if (i[1]+m) >= size[0] or (i[0]+n) >= size[1]:
                            continue
                        h += maskg[i[1]+m, i[0]+n]
                        s += 1
                if h /s > 100:
                    # Light is green, then go
                    self.__light = 1

        if y_circles is not None:

            y_circles = np.uint16(np.around(y_circles))

            for i in y_circles[0, :]:
                if i[0] > size[1] or i[1] > size[0] or i[1] > size[0]*bound:
                    continue

                h, s = 0.0, 0.0
                for m in range(-r, r):
                    for n in range(-r, r):

                        if (i[1]+m) >= size[0] or (i[0]+n) >= size[1]:
                            continue
                        h += masky[i[1]+m, i[0]+n]
                        s += 1
                if h / s > 50:
                    # Light is yellow, then stop
                    self.__light = 0

        # Publish traffic light
        self.pub_light.publish(self.__light)

    ''' Capture a Video '''
    def Capture(self,vid,cap):
        while True:
            ret,frame = vid.read()

            if ret == True:
                try:
                    # Preprocess noise bluring
                    frame = cv.GaussianBlur(frame,(9,9),0)
                    cv.imshow('Video',frame)
                    # Detect traffic lughts
                    self.detect_semaforo(frame)
                    print(f"Semaforo: {self.__light}")

                except: 
                    pass

            elif ret == False:
                print("End of video")
                break

            key = cv.waitKey(1)
            # If Esc key pressed break the process
            if key == 27:
                # Dont show video anymore
                cap = False
                break

        vid.release()
        cv.destroyAllWindows()
        return cap

    ''' Capture Video from Camera '''
    def CaptureMainCamera(self):
        vid = VideoCapture(0)

        while True:
            ret, frame = vid.read()

            if ret == True:
                try:
                    # Preprocess noise bluring
                    frame = cv.GaussianBlur(frame,(9,9),0)
                    cv.imshow('Video',frame)
                    # Detect traffic lughts
                    self.detect_semaforo(frame)
                    print(f"Semaforo: {self.__light}")

                except: 
                    pass

            elif ret == False:
                print("End of video")
                break

            key = cv.waitKey(1)
            # If Esc key pressed break the process
            if key == 27:
                # Dont show video anymore
                cap = False
                break

        vid.release()
        cv.destroyAllWindows()

        return cap


    def Traffic_Light(self):
        ''' Main Code '''
        self.current_time = rospy.get_time()
        self.last_time = rospy.get_time()

        while not rospy.is_shutdown():
            cap = self.CaptureMainCamera() # Capture Video from Camera


if __name__ == "__main__":
    try:
        TL = Detect_Light()
        TL.Traffic_Light()

    except rospy.ROSInterruptException:
        pass