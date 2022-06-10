import cv2
import numpy as np
import functools
from pathlib import Path
import os

def detect_chars(imag, img_name='',showSteps=False):
        """ Detect characters from the given license plate image/array"""

        image = cv2.imread(imag)  # Use this to read an image
        # image = np.array(imag, np.uint8) # Use this to read an array
        
        image = cv2.resize(image,(300,120) )    # Resize the image into 300 x 120
        
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Grayscale the image
        gray = 255-gray # Invert the Image
        gray = cv2.bilateralFilter(gray, 11, 17, 17)    # Filter the image with bilateral Filter 

        # Threshold the image into binary
        thresh = cv2.adaptiveThreshold(gray, 255,
        cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 27, 20)
        
        # Process the image with erode and dilate
        thresh = cv2.erode(thresh, (3,3))
        thresh = cv2.dilate(thresh, (3,3))
        thresh = cv2.dilate(thresh, (3,3))
        thresh = cv2.erode(thresh, (3,3))

        # Mask the image
        _, labels = cv2.connectedComponents(thresh)     # Check all of the groups of white pixels with connectedComponents


        mask = np.zeros(thresh.shape, dtype="uint8")

        # Set lower bound and upper bound criteria for characters
        
        total_pixels = image.shape[0] * image.shape[1]  # Total pixel of the image
        lower = total_pixels // 200 # heuristic param, can be fine tuned if necessary, used to set lower boundary of pixels
        upper = total_pixels // 4 # heuristic param, can be fine tuned if necessary, used to set upper boundary of pixels
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


        # Find contours and get bounding box for each contour
        cnts, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        boundingBoxes = [cv2.boundingRect(c) for c in cnts]

        # # Sort the bounding boxes from left to right
        def takeXelement(elem):
                return elem[0]
        boundingBoxes.sort(key=takeXelement)

        # Create a rectangle on each of the contours
        detected_char_list = []
        out_image = image.copy()
        for c in boundingBoxes:
                x,y,w,h = c

                # Filter to image from the noises at the border of the iamge.
                x = x-2
                y = y-2
                w = w+4
                h = h+4
                if w >10 and w < 50 and h < 80 and h > 20 and x > 2 and x < 290 and y > 2 and y < 60 : 
                        cv2.rectangle(out_image,(x,y),(x+w,y+h),(0,255,0),2)    
                        detected_char_list.append(mask[y:y+h, x:x+w])   # Take all the filtered contours into a detected_char_lsit
        
        # Algorithm to show the steps when showSteps is True
        if showSteps == True:           
                cv2.imshow("Original Image", image)
                cv2.imshow("Grayscaled Image", gray)
                cv2.imshow("Thresholded Image", thresh)
                cv2.imshow("Masked Image",mask)
                cv2.imshow("Detected Image", out_image)

        write_characters(detected_char_list, img_name)  # Take all detected characters into a folder, can be skipped if necessary
        return detected_char_list             # Return all array of detected characters

def write_characters(detected_char_list, img_name):
        """ Input all of the detected characters into a folder """
        i = 1
        path = os.path.join(Path().absolute(), "detected_chars") # Directory of current working directory, not __file__ 
        path = os.path.join(path, img_name[:-3])
        if not os.path.exists(path):
                os.makedirs(path)

        for pic in detected_char_list:  
                cv2.resize(pic, (70,100))
                pic_format = img_name +"test"+str(i)+".jpg" 
                cv2.imwrite(os.path.join(path, pic_format), pic)
                i+=1

def main():
        """ Main Program """
        folder_path = "src_img" # Change the path with the folder with imgs
        path = os.path.join(Path().absolute(),folder_path) # Directory of current working directory, not __file__ 
        
        # Use this code below to detect a characters from a single image
        img = "plat4.jpg" # Change it to the image you want to test
        # Set showSteps to True to see the steps used to detect a characters
        detected_char_list = detect_chars(os.path.join(path, img), img, showSteps=False) 
        
       # Use this code below to detect a characters from all the images inside a folder
        # path_list = os.listdir(path)
        # for img in path_list:
        #         # try:
        #                 # flip(os.path.join(path,img),img)
        #                  mask = detect_chars(os.path.join(path,img), img, showSteps=False)
        #         # except:
        #         #         continue

        cv2.waitKey(0)
if __name__=="__main__":
        main()
