### Just as with the image detector, we now do it with a live feed from our webcam!
# Only difference compared to image: the argument --image is not required, as we use
# VideoStream from imutils. We then read the frames. 
## run using:
#  python detect_video.py --prototxt deploy.prototxt.txt --model res10_300x300_ssd_iter_140000.caffemodel

import cv2
import argparse
import numpy as np
import time
# Imutils has some specific image and video tools specific to openCv2.
import imutils
from imutils.video import VideoStream

# work on the argument parser again. 
ap = argparse.ArgumentParser()
#ap.add_argument('--image', required = True) We will be using video livestream
ap.add_argument('--model', required = True)
ap.add_argument('--prototxt', required = True)
ap.add_argument('--confidence', required = False, default=0.5)
# now add the arguments to the 'list' so that we can later find the arguments easily
# instead of using ap.parse_args('--image')
args = vars(ap.parse_args())

# Let's load the model and pre-trained weights again
print('Loading prototxt and model')
net = cv2.dnn.readNetFromCaffe(args['prototxt'], args['model'])
print('Model and weights loaded. Time for some livefeed! /n SMILE!')
vs = VideoStream(src=0).start()
# Realtime feed fro rasberrypi 
# vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)

while True:
    frame = vs.read()
    frame = imutils.resize(frame, width = 400)
    (h,w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0,
		(300, 300), (104.0, 177.0, 123.0))
    net.setInput(blob)
    detections = net.forward()
    # forward() find us the confidence detections[0, 0, i, 2]
    # and the class label idetections[0, 0, i,1])
    # and the boxpoints detections[0, 0, i, 3:7]
    for i in range(0, detections.shape[2]):
        print(i)
        confidence = detections[0, 0, i, 2]
        if confidence < args['confidence']:
            print('continue')
            continue

        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")
        # start creating the confidence box and give some details
        text = "{:.2f}%".format(confidence * 100)
        y = startY - 10 if startY - 10 > 10 else StartY + 10
        cv2.rectangle(frame, (startX, startY), (endX, endY),
			(0, 0, 255), 2)
        cv2.putText(frame, text, (startX, y),
			cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)


    cv2.imshow('Demo window', frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break        

    if key == ord("c"):
        break   

    if key == ord("z"):
        break   

cv2.destroyAllWindows()
vs.stop()