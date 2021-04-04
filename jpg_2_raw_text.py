# For Linux environments
# If you use pip to install pytesseract 
# sudo apt update
# sudo apt install tesseract-ocr
# sudo apt install libtesseract-dev

import cv2
import pytesseract

img = cv2.imread('/path/to/file/pdf-sample.jpg')
text = pytesseract.image_to_string(img)

with open("/path/to/write/output/output.txt", 'w', encoding='utf-8') as f:
    f.write(text)

f.close()
