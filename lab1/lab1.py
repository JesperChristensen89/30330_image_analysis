import cv2
import sys
from matplotlib import pyplot as plt

## Part 1

if len(sys.argv) == 1:
    image_path = "ariane.jpg"
else:
    image_path = sys.argv[1]


#img = cv2.imread(image_path,flags=cv2.IMREAD_GRAYSCALE)

while True:

    camera = cv2.VideoCapture(0)
    (grabbed, frame) = camera.read()
    cv2.imshow("test",frame)
    cv2.waitKey(0)


#img1 = img
#img1[:,:,1] = 255-img[:,:,1]


#print "Image path: %s" % image_path
#height, width, channels = img.shape

#print "Height: %d Width: %d Channels: %d" % (height, width, channels)

hist = cv2.calcHist([img],[0],None,[256],[0,256])
#hist,bins = np.histogram(img.ravel(),256,[0,256])

#plt.hist(img.ravel(),256,[0,256]); plt.show()