import numpy as np
import cv2

class OCR:

    # for Debug
    DEBUG = True
    
    # OCR variables
    inputImgs = []
    results   = []

    # Constructor
    def __init__(self, inputImgs):
        print "OCR started"

        # Loading input img paths
        self.inputImgs = inputImgs

        # Loading template imgs
        # .......TODO..........

    # Starting OCR
    def start(self):        
        # for each img in the input list
        for path in self.inputImgs:
            # Load image
            img = cv2.imread(path)
            cv2.imshow('ORIGINAL', img)

            # Preparing the image
            img_ready = self.prepareImg(img)

            # Starting Comparison
            # .......TODO........

            # Giving the best result
            # .......TODO........

            cv2.waitKey(0)
            cv2.destroyAllWindows()

        # Returning a list of strings
        return results



    def prepareImg(self, img):
        # Pipeline: BGR -> GrayScale, GrayScale -> BinaryImg, Removing noise
        img_gray = self.convertToGrayScale(img)
        img_bin  = self.performThresholding(img_gray)
        img_dil  = self.performDilate(img_bin)
        return img_dil

    def convertToGrayScale(self, img):
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        if self.DEBUG:
            cv2.imshow('GRAY_SCALE', img_gray)
        return img_gray

    def performThresholding(self, img):
        ret, img_bin = cv2.threshold(img, 160, 255, cv2.THRESH_BINARY_INV)
        if self.DEBUG:
            cv2.imshow('AFTER_THRESHOLDING', img_bin)
        return img_bin

    def performDilate(self, img):
        kernel = np.ones((1, 1), np.uint8)
        img_dil = cv2.dilate(img, kernel, iterations=1)
        erosion = cv2.erode(img_dil,kernel,iterations = 1)
        if self.DEBUG:
            cv2.imshow('AFTER_DILATE', img_dil)
        return img_dil