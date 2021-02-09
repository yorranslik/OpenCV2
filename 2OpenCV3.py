# Now that we know the basics, let's do an excersise. 
# Calculate the number of blocks.

import cv2
import imutils
import argparse


# Build the argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())

# We then use this image to load into cv2
image = cv2.imread(args['image'])
cv2.imshow("Image original", image)


# Convert to BW, which makes it easier for us to do edge detection. 
bw = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Black and white", bw)

## Canny
# To further enhance this, we use canny, a specific algortm for edge detection. 
# We give the image, the minimal value (threshold) and the max. 
edged = cv2.Canny(bw, 30, 150)
cv2.imshow("Edged", edged)


## Thresholding
# Then comes a difficult part, which is a lot of trial and error. Thresholding.
# Thresholding can help us to remove lighter or darker regions and contours of images
thresh = cv2.threshold(bw, 225, 255, cv2.THRESH_BINARY_INV)[1]
cv2.imshow("Thresh", thresh)

## Contours
# Now that we have very clear lines, lets see if we can make some lines!
# We first need to find the contours using the built in function. We then loop
# iver them.  
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
output = image.copy()

for c in cnts:
	# draw each contour on the output image with a 3px thick purple
	# outline, then display the output contours one at a time
	cv2.drawContours(output, [c], -1, (240, 0, 159), 3)
	cv2.imshow("Contours", output)

# Based on what we learned earlier, we can now also add some text! 
print("we have found {} contours".format(len(cnts)))
text = "I found {} objects!".format(len(cnts))
cv2.putText(output, text, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX, 0.7,
	(240, 0, 159), 2)
cv2.imshow("Contours", output)

## Erosions and dilations
# to reduce the size of objects at the fregrond, we can erode some pixels.
# Eroding makes them smaller, dilating makes them bigger!
mask = thresh.copy()
mask = cv2.erode(mask, None, iterations=5)
cv2.imshow("Eroded", mask)

# Dilated
mask = thresh.copy()
mask = cv2.dilate(mask, None, iterations=5)
cv2.imshow("Dilated", mask)

cv2.waitKey(0)