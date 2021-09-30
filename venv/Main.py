from imutils.perspective import four_point_transform
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
vidcap = cv2.VideoCapture('testVideo.mp4')
success, image = vidcap.read()

def main():
    print('Hello World');

if __name__ == "__main__":
    main();