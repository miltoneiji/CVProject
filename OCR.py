import numpy as np
import cv2
from matplotlib import pyplot as plt

class OCR:

    # for Debug
    DEBUG = True
    
    # OCR variables
    trainingImgsPath = ["A.png", "A2.png", "B.png", "B2.png", "C.png", "C2.png", "D.png", "D2.png",
                        "E.png", "E2.png", "F.png", "F2.png", "G.png", "G2.png", "H.png", "H2.png",
                        "I.png", "I2.png", "J.png", "J2.png", "K.png", "K2.png", "L.png", "L2.png",
                        "M.png", "M2.png", "N.png", "N2.png", "O.png", "O2.png", "P.png", "P2.png",
                        "Q.png", "Q2.png", "R.png", "R2.png", "S.png", "S2.png", "T.png", "T2.png",
                        "U.png", "U2.png", "V.png", "V2.png", "W.png", "W2.png", "X.png", "X2.png",
                        "Y.png", "Y2.png", "Z.png", "Z2.png"]
    trainingImgs = []
    inputImgs    = []
    results      = []

    # Constructor
    def __init__(self, inputImgs):
        print "OCR started"

        # Loading input img paths
        self.inputImgs = inputImgs

        # Loading template imgs
        for path in self.trainingImgsPath:
            img = cv2.imread("training/" + path)
            self.trainingImgs.append(img)

    # Starting OCR
    def start(self):        
        # for each img in the input list
        for path in self.inputImgs:
            # Load image
            img = cv2.imread(path)
            cv2.imshow('ORIGINAL', img)

            # Preparing the image
            height, width, channels = img.shape
            resized_img = cv2.resize(img, (width*7, height*7)) 
            img_ready = self.prepareImg(resized_img)

            # Finding contours
            imgCountor, contours, hierarchy = cv2.findContours(img_ready, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            # Drawing
            for i in range(0, len(contours)):
                cv2.drawContours(img_ready, contours, i, (255, 255, 255), 1)
                cv2.imshow('final', img_ready)
                cv2.waitKey(0)

            # Extracting each character


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
        img_ero  = self.performErosion(img_bin)
        img_dil  = self.performDilatation(img_ero); 
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

    def performErosion(self, img):
        kernel = np.ones((9, 9), np.uint8)
        erosion = cv2.erode(img,kernel,iterations = 1)
        if self.DEBUG:
            cv2.imshow('AFTER_EROSION', erosion)
        return erosion

    def performDilatation(self, img):
        kernel = np.ones((5, 5), np.uint8)
        dil = cv2.dilate(img,kernel,iterations = 1)
        if self.DEBUG:
            cv2.imshow('AFTER_DILATE', dil)
        return dil

