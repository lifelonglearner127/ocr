import argparse

import cv2
import imutils
import pytesseract
from pytesseract import Output

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to image")

args = ap.parse_args()
image = cv2.imread(args.image)
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

results = pytesseract.image_to_osd(rgb, output_type=Output.DICT)

# display the orientation information
print(f"[INFO] detected orientation: {results['orientation']}")
print(f"[INFO] rotate by {results['rotate']} degrees to correct")
print(f"[INFO] detected script: {results['script']}")
rotated = imutils.rotate_bound(image, results["rotate"])
cv2.imshow("Original", image)
cv2.imshow("Output", rotated)
cv2.waitKey(0)
