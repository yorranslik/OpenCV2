# Learning OpenCV2 using PY Image Search and the book

This folder serves as a collection of trial and error on my way to learning Image recognition. I've learned the basics at University an lately followed Andrew NGs Deep Learning course. However, I felt that I was lacking the skillset to actually develop things using DL. Hence, I started working with the OpenCV2 framework. Ultimately, I would like to create an ADAS tool using image recognition. The first step, is probablyt the most common one. Learning to detect faces using pre-trained weights and models. 

I would like to appologize for the mess this folder may be. To me, it sort of makes sense in the learning process. Also, the project is not intended to go live. If ever doubting about going live with this: review the project thorougly! 


## Getting Started

This folder contains several scripts that are run using various commants. The commands are listed below. The scripts are:
* Detecting Faces
* Detecting faces with webcam feed
* More to follow shortly. 

#### Prerequisites

Just install cv2 and imutils. Oh, and argpars. The project also uses some other libs, but you'll probably have them allready 

## Face detection using images

Want to detect creepy faces on blacked-out images? Use this. If you dare. Just a plain-simple face detector. It was my first time working with the argparser lib. Fun to do! 
```
python detect_faces.py --image linkedin.jpg --prototxt deploy.prototxt.txt --model res10_300x300_ssd_iter_140000.caffemodel
```

## Face detection using web cam

Smile to your webcam and check whether or not your human. 
```
python detect_video.py --prototxt deploy.prototxt.txt --model res10_300x300_ssd_iter_140000.caffemodel
```

## Basic OpenCV
In the files starting with a 2, I worked on the basic building blocks that OpenCV has, together with imutils. In the first file, I worked on the basic image reading, finding the shape, resizing, finding the color of a specific pixel and rotating. In the second document, I followed online tutorials to learn how to draw ROI boxes, add Gaussian blurr and add text to the the boxes. In the final document, it all came together, including some argparser lessons from yesterday. Here, we learnt to detect edges by converting to grayscale/B&W, add a canny filter, apply thresholding and use the cv2.findcontours() function. With these contours, we then drew the contours using cv2.drawContours(). At the end, the file erodes the objects (smaller) and dilutes (bigger). 

```
python 2OpenCV.py / 2OpenCV2.py
```
```
python 2OpenCV3.py --i tetris_blocks.png
```

## Making a basic document scanner.
some easypiecie documentscanner that transforms the image, detects edges, draws the contours and then waprs the image to give it some smeck. Requires a pyimagesearch function to run properly.

```
python 3Scanner.py --image page.jpg 

```

## Making an exam tester.
Using the stuff we learned yesterday, we import a multiple choice exam and then find which one is filled out using binairy thresholding. This could be extented further to actually find double fills and empty fills, etc. But for now, this is sufficient. Now onto the book. 
```
python 4Exam.py --image omr_test1.png 

```
## selecting and tracking/tracing based on color.
If we would like to trace an object based on the color of the object, we gan use this script. We input the color, and add a tracer. also, this script has some information on how to select either the webcam-feed, or the video input file. 
```
python 5objectdetection.py /--video filename.mp4

```



## Contributing

Feel free to contribute, and above all upgrade.


## Acknowledgments

I would like to take my hat of to you! 
