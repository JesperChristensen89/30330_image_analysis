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
            roi = img[y:y + 2, x:x + 2]
            img_LP1[y, x] = np.median(roi)

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

    test = img[0:20,0:20]
    test1 = np.zeros((20,20),np.uint8)
    for x in range(0,20):
        for y in range(0,20):
            test1[y,x] = (test[y,x])
            #print x,y

    cv2.imshow("test", test1)
    #ar = np.array([[1,2,3],
    #               [4,5,6],
    #               [7,8,9]])
    #print int(np.median(ar))






cv2.waitKey(0)