import argparse
import math
import numpy as np
from matplotlib import pyplot as plt
import cv2
import time

# argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--part", required=True,
                help = "Part of excercise you want to run")
args = vars(ap.parse_args())

part = int(args['part'])

# load, show, resize image
img_orig = cv2.imread('../img/1.JPG')
img_orig = cv2.resize(img_orig, (600,400))
cv2.imshow("Original", img_orig)
cv2.moveWindow("Original",10,10)

img = cv2.cvtColor(img_orig,cv2.COLOR_BGR2GRAY)
height, width = img.shape
print "Shape of img: %dx%d" % (width, height)

if part == 1:

    img_LP1 = np.zeros((height - 2, width - 2), np.uint8)
    for x in range(width - 2):
        for y in range(height - 2):
            roi = img[y:y + 3, x:x + 3]

            roi_flat = np.hstack(roi)

            img_LP1[y, x] = sum(roi_flat)/len(roi_flat)


    cv2.imshow("Low-pass-man", img_LP1)
    cv2.moveWindow("Low-pass-man", width + 20, 10)

    # using filter2d
    kernel = np.ones((3,3),np.float32)/9
    img_LP = cv2.filter2D(img,-1,kernel)

    cv2.imshow("Low-pass", img_LP)
    cv2.moveWindow("Low-pass", width+20, 10)

if part == 2:

    kernel = np.array([[0,1,0],
                       [1,-4,1],
                       [0,1,0]])
    img_HP = cv2.filter2D(img,-1,kernel)

    cv2.imshow("High-pass", img_HP)
    cv2.moveWindow("High-pass", width + 20, 10)


if part == 3:

    t1 = time.time()
    img_median = cv2.medianBlur(img,3)
    print "Median filter using OpenCv: %fs" % (time.time()-t1)

    cv2.imshow("Median", img_median)
    cv2.moveWindow("Median", width + 20, 20)

    t2 = time.time()
    img_med = np.zeros((height-2,width-2),np.uint8)
    for x in range(width-2):
        for y in range(height-2):
            roi = img[y:y+2,x:x+2]
            img_med[y,x] = np.median(roi)
            #print img_med[y,x]

    print "Median filter using own algorithm: %fs" % (time.time() - t2)
    cv2.imshow("Med_self", img_med)
    cv2.moveWindow("Med_self", width + 20, 10)

if part == 4:

    kernel = np.array([[0,0,1,2,2,2,1,0,0],
                       [0,1,5,10,12,10,5,1,0],
                       [1,5,15,19,16,19,15,5,1],
                       [2,10,19,-19,-64,-19,19,10,2],
                       [2,12,16,-64,-148,-64,16,12,2],
                       [2,10,19,-19,-64,-19,19,10,2],
                       [1, 5, 15, 19, 16, 19, 15, 5, 1],
                       [0, 1, 5, 10, 12, 10, 5, 1,0],
                       [0, 0, 1, 2, 2, 2, 1, 0, 0]])


    img_HP = cv2.filter2D(img, -1, kernel)
    cv2.imshow("Laplacian", img_HP)
    cv2.moveWindow("Laplacian", width + 20, 10)

    while True:
        camera = cv2.VideoCapture(0)
        (grabbed, frame) = camera.read()
        frame = cv2.filter2D(frame,-1,kernel)
        cv2.imshow("test", frame)
        cv2.waitKey(0)





cv2.waitKey(0)