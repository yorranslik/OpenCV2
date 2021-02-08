# OpenCV has a 'hidden' Deep learning Face detector. 
# We will work with this on images and video.
# This model is based on Caffe


# Importing libs
import numpy as np
import argparse
import cv2

# Constructing --arguments and parse using the argparse module.
# The argparse modules makes it easy to write user-friendly command-line interfaces.
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "path to the image")
ap.add_argument('-p', '--prototxt', required = True, help = "Path to the protxt file (weights of caffe)")
ap.add_argument('-m', '--model', required= True)
ap.add_argument('-c', '--confidence', required = False, type = float, default = 0.5)
args = vars(ap.parse_args())

## Here we work on the model itself.
print('model loading section')

# We work with a specif caffe dnn option. 
# Documentation: Reads a network model stored in Caffe framework's format.
net = cv2.dnn.readNetFromCaffe(args['prototxt'], args['model'])
#net = cv2.dnn.readNetFromCaffe(ap.parse_args('--proxtx'), ap.parse_args('--model'))

image = cv2.imread(args['image'])
#image = cv2.imread(ap.arg_parse('--image'))
(h,w) = image.shape[:2]
blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0,
	(300, 300), (104.0, 177.0, 123.0))

print("Model loading succesfull.  \n Now lets do some calculations")
# Loading the image into net (which we defined above)
net.setInput(blob)
detections = net.forward()

# forward() find us the confidence detections[0, 0, i, 2]
# and the class label idetections[0, 0, i,1])
# and the boxpoints detections[0, 0, i, 3:7]

print("We have detections:", detections.shape[2], " and will loop all over them")

# start looping over the various detections (detections.shape)
for i in range(0, detections.shape[2]):
    confidence = detections[0,0,i,2]
    print(i)
    if confidence > args['confidence']:
        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")
        # start creating the confidence box and give some details
        text = "{:.2f}%".format(confidence * 100)
        y = startY - 10 if startY - 10 > 10 else StartY + 10
        cv2.rectangle(image, (startX, startY), (endX, endY),
			(0, 0, 255), 2)
        cv2.putText(image, text, (startX, y),
			cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)


# Showing output
cv2.imshow("Output of this demo", image)
cv2.waitKey(0)
