import cv2
import imutils


# Once again, we start with imread, then get our shape in w,h,d sizing and show the image
# afterwwards we give a waitkey, otherwise it closes very quickly. 
image = cv2.imread('jp.png')
(w,h,d) = image.shape
print("dimensions are {} width, {} height and {} depth".format(w,h,d))
cv2.imshow("WindowName", image)

## Blurring
# In many image processing pipelines, we must blur an image to reduce high-frequency 
# noise, making it easier for our algorithms to detect and understand the actual contents 
# of the image rather than just noise that will “confuse” our algorithms
# Let's start with the Gaussianblur. The blurring kernal in (10,10) can be played
# with, as a larger kernel creates more blur. Blur kernals need to be odd.

blurred = cv2.GaussianBlur(image, (111,111), 0 )
#cv2.imshow("Blurred", blurred)

## Drawing
# Using OpenCV we can add boxes around our pciture. Let's start with the basics.
# always copy first, as drawing action overwrite our image variable.
# the function is easy rectangle(image, (top-left), (bottom-right), (BGR tupple), thickness)
# circles and lines work the same way.
image2 = image.copy()
cv2.rectangle(image2, (320, 60), (420, 160), (0, 0, 255), 2)
cv2.circle(image2, (300, 150), 20, (255, 0, 0), 1)
cv2.line(image2, (60, 20), (400, 200), (0, 0, 255), 1)
cv2.imshow("Rectangle and circle + line", image2)

## Adding text
# Additonally, we can add text, which is obviously highly needed sometimes.
# This is well documented, and has a lot of parameters, so just use this.
output = image.copy()
cv2.putText(output, "My little OpenCv practise", (10, 25), 
	cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
cv2.imshow("Wollah", output)



cv2.waitKey(0)
