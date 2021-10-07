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


#thresh = cv2.adaptiveThreshold(warped,  255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
#                       cv2.THRESH_BINARY, 11, 2)
blur = cv2.GaussianBlur(warped, (3, 3), 0)
ret, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
#kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 2))
#thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2. CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
digitCnts = []

# for c in cnts:
#     (x,y,w,h) = cv2.boundingRect(c)
#
#
#     if w >= 15 and (h >= 30 and h <= 40):
#         digitCnts.append(c)
#         cv2.rectangle(thresh, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
# digitCnts = contours.sort_contours(digitCnts, method="left-to-right")[0]
# plt.imshow(thresh)
# digits = []

# for c in digitCnts:
# 	# extract the digit ROI
# 	(x, y, w, h) = cv2.boundingRect(c)
# 	roi = thresh[y:y + h, x:x + w]
# 	# compute the width and height of each of the 7 segments
# 	# we are going to examine
# 	(roiH, roiW) = roi.shape
# 	(dW, dH) = (int(roiW * 0.25), int(roiH * 0.15))
# 	dHC = int(roiH * 0.05)
# 	# define the set of 7 segments
# 	segments = [
# 		((0, 0), (w, dH)),	# top
# 		((0, 0), (dW, h // 2)),	# top-left
# 		((w - dW, 0), (w, h // 2)),	# top-right
# 		((0, (h // 2) - dHC) , (w, (h // 2) + dHC)), # center
# 		((0, h // 2), (dW, h)),	# bottom-left
# 		((w - dW, h // 2), (w, h)),	# bottom-right
# 		((0, h - dH), (w, h))	# bottom
# 	]
# 	on = [0] * len(segments)
#
#     # loop over the segments
# for (i, ((xA, yA), (xB, yB))) in enumerate(segments):
#     # extract the segment ROI, count the total number of
#     # thresholded pixels in the segment, and then compute
#     # the area of the segment
#     segROI = roi[yA:yB, xA:xB]
#     total = cv2.countNonZero(segROI)
#     area = (xB - xA) * (yB - yA)
#     # if the total number of non-zero pixels is greater than
#     # 50% of the area, mark the segment as "on"
#     if total / float(area) > 0.5:
#         on[i] = 1
#     # lookup the digit and draw it on the image
# digit = DIGITS_LOOKUP[tuple(on)]
# digits.append(digit)
# cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 1)
# cv2.putText(output, str(digit), (x - 10, y - 10),
#             cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 255, 0), 2)
#
# # display the digits
# print(u"{}{}.{} \u00b0C".format(*digits))
# cv2.imshow("Input", image)
# cv2.imshow("Output", output)
# cv2.waitKey(0)

def showImage(image):
    plt.imshow(image)
    plt.show()

def main():
    showImage(image)
    showImage(edged)
    showImage(warped)
    showImage(output)
    showImage(thresh)
    print("DIGITS FOUND: " + str(len(digitCnts)))

if __name__ == "__main__":
    main();