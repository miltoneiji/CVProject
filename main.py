import numpy as np
import cv2

DEBUG = True

# Entry point
def main():
    # Loading image
    img = cv2.imread('input/door.png')

    # Pipeline
    img_gray = convertToGrayScale(img)
    img_bin  = performThresholding(img_gray)
    img_dil  = performDilate(img_bin)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def convertToGrayScale(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if DEBUG:
        cv2.imshow('GRAY_SCALE', img_gray)
    return img_gray

def performThresholding(img):
    ret, img_bin = cv2.threshold(img, 160, 255, cv2.THRESH_BINARY_INV)
    if DEBUG:
        cv2.imshow('AFTER_THRESHOLDING', img_bin)
    return img_bin

def performDilate(img):
    kernel = np.ones((1, 1), np.uint8)
    img_dil = cv2.dilate(img, kernel, iterations=1)
    erosion = cv2.erode(img_dil,kernel,iterations = 1)
    if DEBUG:
        cv2.imshow('AFTER_DILATE', img_dil)
    return img_dil

if __name__ == '__main__':
    main()