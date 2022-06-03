import cv2
import imutils
import numpy as np

import functools
from pathlib import Path
import os

def connected(image, showSteps=False):
        image = cv2.imread(image)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = 255-gray
        gray = cv2.bilateralFilter(gray, 11, 17, 17) 
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        thresh = cv2.adaptiveThreshold(blurred, 255,
        cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 45, 15)
        
        _, labels = cv2.connectedComponents(thresh)

        print(labels)
        mask = np.zeros(thresh.shape, dtype="uint8")

        # Set lower bound and upper bound criteria for characters
        total_pixels = image.shape[0] * image.shape[1]
        lower = total_pixels // 170 # heuristic param, can be fine tuned if necessary
        upper = total_pixels // 5 # heuristic param, can be fine tuned if necessary
        # Loop over the unique components
        for (i, label) in enumerate(np.unique(labels)):
                # If this is the background label, ignore it
                if label == 0:
                        continue
                # Otherwise, construct the label mask to display only connected component
                # for the current label
                labelMask = np.zeros(thresh.shape, dtype="uint8")
                labelMask[labels == label] = 255
                
                numPixels = cv2.countNonZero(labelMask)
        
                # If the number of pixels in the component is between lower bound and upper bound, 
                # add it to our mask
                if numPixels > lower and numPixels < upper:
                        mask = cv2.add(mask, labelMask)
        if showSteps == True:
                cv2.imshow("thresh", thresh)
                cv2.imshow("gray", gray)
                cv2.imshow("mask",mask)

        # Find contours and get bounding box for each contour
        cnts, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        boundingBoxes = [cv2.boundingRect(c) for c in cnts]

        # # Sort the bounding boxes from left to right, top to bottom
        # # sort by Y first, and then sort by X if Ys are similar
        def compare(rect1, rect2):
                if abs(rect1[1] - rect2[1]) > 10:
                        return rect1[1] - rect2[1]
                else:
                        return rect1[0] - rect2[0]

        boundingBoxes = sorted(boundingBoxes, key=functools.cmp_to_key(compare))
        charpic = []
        new_mask = mask.copy()
        for c in boundingBoxes:
                x,y,w,h = c
                x = x-2
                if y-2 >=0:
                        y = y-2
                w = w+2
                h = h+2
                if w>5 and h>10: 
                        cv2.rectangle(new_mask,(x,y),(x+w,y+h),(255,255,0),3)
                        charpic.append(mask[y:y+h, x:x+w])
        cv2.imshow("detected_char",new_mask)
        crop(charpic)
        return mask

def crop(charpic):
        i = 1
        path = os.path.join(Path().absolute(), "detected_chars") # Directory of current working directory, not __file__ 
        if not os.path.exists(path):
                os.makedirs(path)
        for pic in charpic:                
                pic_format = "test"+str(i)+".jpg" 
                cv2.imwrite(os.path.join(path, pic_format), pic)
                i+=1
def detect_plate(imag, showSteps = False):
        image = cv2.imread(imag)
       
        image = cv2.resize(image, (300,130))

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = 255-gray
        gray = cv2.GaussianBlur(gray,(5,5),0)
        gray = cv2.bilateralFilter(gray, 11, 17, 17) 

        edged = cv2.Canny(gray, 30, 200) 
        cnts,new = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        image1=image.copy()
        cv2.drawContours(image1,cnts,-1,(0,255,0),3)

        cnts = sorted(cnts, key = cv2.contourArea, reverse = True) [:60]
        screenCnt = None
        image2 = image.copy()
        cv2.drawContours(image2,cnts,-1,(0,255,0),3)

        i=1
        for c in cnts:
                perimeter = cv2.arcLength(c, True)
                approx = cv2.approxPolyDP(c, 0.018 * perimeter, True)
                if len(approx) == 4: 
                        screenCnt = approx
                        x,y,w,h = cv2.boundingRect(c) 
                        new_img=image[y:y+h,x:x+w]
                        cv2.imwrite('./'+str(i)+'.jpg',new_img)
                        i+=1
                        break
        if showSteps == True:
                cv2.imshow("Original Image", image)
                cv2.imshow("B&W Image", gray)
                cv2.imshow("Canny Image", edged)
                cv2.imshow("Contours",image1)
                cv2.imshow("Top 30 contours",image2)

        if screenCnt is not None:
                cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 3)
                cv2.imshow("image with detected license plate", image)
                return i-1
        else:
                print("Image not detected")
                return -1

def main():
        path = os.path.join(Path().absolute(), "src_img") # Directory of current working directory, not __file__ 
        a = detect_plate(os.path.join(path,"test_img.jpg"), showSteps=False)
        # if a is not -1:
        #         a = str(a) + ".jpg"
        #         mask = connected(a, showSteps=True)

        cv2.waitKey(0)
if __name__=="__main__":
        main()
