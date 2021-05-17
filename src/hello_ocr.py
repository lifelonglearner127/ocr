import argparse

import cv2
import pytesseract

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to image")
ap.add_argument("-d", "--digits", action="store_true", help="whether or not *digits only* OCR will be performed")
ap.add_argument("-w", "--whitelist", type=str, default="", help="list of characters to whitelist")
ap.add_argument("-b", "--blacklist", type=str, default="", help="list of characters to blacklist")

args = ap.parse_args()
image = cv2.imread(args.image)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
options = ""
if args.digits:
    options += "outputbase digits"
if args.whitelist:
    options += f"-c tessedit_char_whitelist={args.whitelist}"
if args.blacklist:
    options += f"-c tessedit_char_blacklist={args.blacklist}"

text = pytesseract.image_to_string(image, config=options)
print(text)
