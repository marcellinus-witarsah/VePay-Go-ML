# Character Segmentation

## Introduction
This is an API used to segmentate the characters from the given detected license plate obtained from license-plate-object-detection API. There are 2 programs provided, char_segmentations.py for python and opencv_js folder for the javascript version of the program.

## Requirements
- Python installed in Local Machine

## Libraries
- OpenCV
- Numpy

## Environment Settings
This API can be run on any device that supports C language as OpenCV originally are a C program language. For starters, clone this repository into your local machine with:

```git clone https://github.com/marcellinus-witarsah/VePay-Go-ML.git```

To use this API, install the required libraries with pip.

- ```pip install opencv-python``` 
- ```pip install numpy```

## API Details
Two function are used on this API, **detect_chars** function as the main program and **write_characters** function to convert all of the detected characters into images inside a folder(OPTIONAL).

**"detect_chars"**: 

This function are used to return a list of the ROI of all the detected characters. Three inputs are required, first is the PATH to the images, second is the image name, and the third is to show the steps by the OpenCV.

**"write_characters"**: 

This function are used to write all of the detected characters into an image inside a folder. Two inputs are required, first input is the list of ROI and the second input is the image name. 

To display the steps used by the OpenCV, change the ```showSteps=False``` on the **detect_chars** function into ```showSteps=True``` when calling the function.
