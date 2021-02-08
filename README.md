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

## Contributing

Feel free to contribute, and above all upgrade.


## Acknowledgments

I would like to take my hat of to you! 
