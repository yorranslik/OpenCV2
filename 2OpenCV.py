## Lets dive into the basics of OpenCV.

# We always need OpenCV and imutils installed and obviously some content.
import imutils
import cv2


# Then we read an image, and find its dimensions (as the dimensions are shown as as
# a Numpy Array) with h,w,depth. 
# we read an image using imread and display it using imshow("framename", image)
# we always close with a cv.waitkey(0) at the very bottom.

image = cv2.imread( "jp.png") # converts it just a numpy array.
(w,h,d) = image.shape   
print("dimensions are {} width, {} height and {} depth".format(w,h,d))
cv2.imshow("Framenaam", image)

# Now, let's see if we can find some pixel values. But, just like opencv
# stores shape as height, width and depth. For colors it also does something strang.
# It stores is at BGR. This is the pixel color at 1 specific location. 
(B, G, R) = image[100, 50]
print("R={}, G={}, B={}".format(R, G, B))

# Now suppose we want to find ROI, or, an interesting section of the picture.
# We can slice it manually.. 
roi = image[60:160, 320:420]
cv2.imshow("ROI manualy sliced", roi)

# Resizing can also be needed (especially when working with large frames)
# For resizing, we simply give the frame we want to size to the resize function
# as well as the desired format.
resized = cv2.resize(image, (100,100))
cv2.imshow("Resized image 100x100", resized)

# However, this may distort our ratio, we can calculate it with hand. Luckily imutils also has an option for us.
resized2 = imutils.resize(image, width=300) # or use height
cv2.imshow("Imutils resized image", resized2)

# Rotating is slighlty more difficult, as first need the centre of the image.
# However, obviously, the center is exactly the middle. so we divide the height and width with 2,
# and voila! There we go. Using this, we can a rotationmatrix.
# Using this rotation matrix, we give the center, the degrees we want to turn.
# After flipping the matrix, we need to warp the image, which actually does the rotation.
# after this, we quickly check a quicker method!!! So you might skip this.
center = (w //2, h //2)
M = cv2.getRotationMatrix2D(center, -45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("OpenCV Rotation", rotated)

## Quicker method
rotated = imutils.rotate(image, -45)
cv2.imshow("Imutitls Rotation", rotated)

# Now, if we want to keep the entire image and have it rotated: 
rotated = imutils.rotate_bound(image, 45)
cv2.imshow("Imutils Bound Rotation", rotated)

cv2.waitKey(0)


