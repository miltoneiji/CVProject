import glob
from OCR import OCR

# Entry point
def main():
    # Loading input images
    inputImgs = glob.glob('input/*.png')

    # Starting OCR
    ocr = OCR(inputImgs)
    results = ocr.start()

    # Printing
    print results

if __name__ == '__main__':
    main()