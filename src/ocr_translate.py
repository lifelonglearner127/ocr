import argparse

import cv2
import pytesseract
from textblob import TextBlob

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to image")
ap.add_argument(
    "-l", "--lang", type=str, default="es", help="language to translate OCR'd text to (default is Spanish)"
)

args = ap.parse_args()
image = cv2.imread(args.image)
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

text = pytesseract.image_to_string(rgb)
text = text.replace("\n", " ")
# show the original OCR'd text
print("ORIGINAL")
print("========")
print(text)

tb = TextBlob(text)
translated = tb.translate(to=args.lang)
print("TRANSLATED")
print("==========")
print(translated)
