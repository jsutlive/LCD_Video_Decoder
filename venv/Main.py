from imutils.perspective import four_point_transform
import matplotlib.pyplot as plt
from imutils import contours
import imutils
import cv2
import os
#describe each number on a seven-segment display as a series of on/off switches
DIGITS_LOOKUP = {
    (1,1,1,0,1,1,1) : 0,
    (0,0,1,0,0,1,0) : 1,
    (1,0,1,1,1,1,0) : 2,
    (0,1,1,1,0,1,1) : 3,
    (0,1,1,1,0,1,0) : 4,
    (1,1,0,1,0,1,1) : 5,
    (1,1,0,1,0,1,1) : 6,
    (1,0,1,0,0,1,0) : 7,
    (1,1,1,1,1,1,1) : 8,
    (1,1,1,1,0,1,1) : 9
}

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
vidcap = cv2.VideoCapture(ROOT_DIR + '\\testVideo.mp4')
success, image = vidcap.read()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray,(5,5),0)
edged = cv2.Canny(blurred, 50,200,255)
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts,key=cv2.contourArea, reverse=True)
displayCnt = None

for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)

    if len(approx) == 4:
        displayCnt = approx
        break

warped = four_point_transform(gray, displayCnt.reshape(4, 2))
output = four_point_transform(image, displayCnt.reshape(4, 2))

def showImage(image):
    plt.imshow(image)
    plt.show()

def main():
    showImage(image)
    showImage(edged)
    showImage(warped)
    showImage(output)

if __name__ == "__main__":
    main();