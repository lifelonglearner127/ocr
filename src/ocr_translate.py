import argparse

import cv2
import pytesseract
from textblob import TextBlob

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to image")
ap.add_argument(
    "-l", "--lang", type=str, default="en", help="language that Tesseract will use when OCR'ing(default is English)"
)
ap.add_argument("-t", "--to", type=str, default="es", help="language to translate OCR'd text to (default is Spanish)")
ap.add_argument("-p", "--psm", type=int, default=13, help="Tesseract PSM mode")
args = ap.parse_args()
image = cv2.imread(args.image)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

options = f"-l {args.lang} --psm {args.psm}"
text = pytesseract.image_to_string(image, config=options)
text = text.replace("\n", " ")
# show the original OCR'd text
print("ORIGINAL")
print("========")
print(text)

tb = TextBlob(text)
translated = tb.translate(to=args.to)
print("TRANSLATED")
print("==========")
print(translated)
