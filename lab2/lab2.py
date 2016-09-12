import argparse
import math
import numpy as np
from matplotlib import pyplot as plt
import cv2

def ImageHistogram(img_in):
    img_out = np.ones((600, 600), np.uint8) * 255
    grey_color = 125
    # x-axis draw
    img_out[560, 35:555] = grey_color
    # y-axis draw
    img_out[15:565, 40] = grey_color
    # 255 tap
    img_out[560:565, 552] = grey_color
    # draw values
    cv2.putText(img_out, '0', (35, 585), cv2.FONT_HERSHEY_SIMPLEX, 0.5, grey_color, 2)
    cv2.putText(img_out, '255', (530, 585), cv2.FONT_HERSHEY_SIMPLEX, 0.5, grey_color, 2)

    hist = cv2.calcHist([img_in], [0], None, [256], [0, 256])
    hist = hist / np.amax(hist) * 550
    hist = hist.astype(int)
    i = 0
    for val in hist:
        img_out[(565 - val[0]):560, i + 41:i + 43] = grey_color
        i += 2
    return img_out

# argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--part", required=True,
                help = "Part of excercise you want to run")
args = vars(ap.parse_args())

# load input image - static for this lab excercise
img = cv2.imread("../img/PEN.pgm",cv2.IMREAD_GRAYSCALE)
heigth, width = img.shape
print "Input image size: {0}x{1}".format(width, heigth)

# get part arg
part = int(args["part"])


print "Running part: %s" % (part)

if part == 1: ## Part 1 - image thresholding

    #print "Input image size: {0}x{1}".format(width, heigth)

    img1 = img.copy()

    cv2.imshow("Original image", img)
    cv2.moveWindow("Original image", 10, 10)

    img1 = cv2.threshold(img,125,255, cv2.THRESH_BINARY)[1]

    cv2.imshow("Modified image", img1)
    cv2.moveWindow("Modified image", width+20, 10)

    #hist = ImageHistogram(img.copy())

    #cv2.imshow("Histogram", hist)
    #cv2.moveWindow("Histogram", 2*width + 2*20, 10)

    #cv2.waitKey(0)

    hist = cv2.calcHist([img],[0],None,[256],[0,256])
    fig = plt.hist(img.ravel(),256,[0,256])
    #plt.get_current_fig_manager().window.setGeometry(2*width+30,10,500,heigth)
    axes = plt.gca()
    axes.set_xlim([0,255])
    plt.show()

   
elif part == 2: ## Part 2 - Center off mass

    img1 = img.copy()



    __, img1 = cv2.threshold(img,125,255, cv2.THRESH_BINARY)
    __, contours, __ = cv2.findContours(img1.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    contour = contours[1]

    M = cv2.moments(contour)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])

    print cx, cy

    img_color = img.copy()
    img_color = cv2.cvtColor(img_color,cv2.COLOR_GRAY2RGB)

    # draw some stuff
    cv2.drawContours(img_color, [contour], 0, (0,255,0), 3)
    #cv2.putText(img_color,"X", (20,20), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
    cv2.circle(img_color, (cx, cy), 3, (255,255,0), -1)

    cv2.imshow("Original image", img_color)
    cv2.moveWindow("Original image", 10, 10)

    cv2.imshow("Modified image", img1)
    cv2.moveWindow("Modified image", width+20, 10)

    cv2.waitKey(0)

elif part == 3: ## Part 3 - Image moments

    img1 = img.copy()


    __, img1 = cv2.threshold(img,125,255, cv2.THRESH_BINARY)
    __, contours, __ = cv2.findContours(img1.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    contour = contours[1]

    img_color = img.copy()
    img_color = cv2.cvtColor(img_color,cv2.COLOR_GRAY2RGB)



    # draw some stuff
    cv2.drawContours(img_color, [contour], 0, (0,255,0), 3)

    M = cv2.moments(contour)
    nu_20 = int(M['mu20'])/int(M['m00'])
    nu_02 = int(M['mu02'])/int(M['m00'])
    nu_11 = int(M['mu11'])/int(M['m00'])

    print "nu_20: {0} nu_02: {1} nu_11: {2}".format(nu_20, nu_02, nu_11)

    tilt = math.atan(2*nu_11/(nu_20-nu_02))/2

    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])

    line_lengt = 100

    x1 = cx + line_lengt * math.cos(tilt-math.pi/2)
    x1 = int(x1)
    y1 = cy + line_lengt * math.sin(tilt-math.pi/2)
    y1 = int(y1)

    cv2.line(img_color,(cx,cy),(x1,y1),(0,255,0),1)

    x1 = cx + line_lengt * math.cos(tilt)
    x1 = int(x1)
    y1 = cy + line_lengt * math.sin(tilt)
    y1 = int(y1)

    cv2.line(img_color, (cx, cy), (x1, y1), (0, 255, 0), 1)

    print "Tilt of object: {0}deg".format(tilt*180/math.pi)

    cv2.imshow("Original image", img_color)
    cv2.moveWindow("Original image", 10, 10)

    cv2.imshow("Modified image", img1)
    cv2.moveWindow("Modified image", width+20, 10)



    cv2.waitKey(0)
