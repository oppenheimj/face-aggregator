# face-aggregator
<img src='docs/images/face_logo.png' width=131>

# Introduction

Ever take many pictures of the same scene and there's never a perfect one? We have the solution for you!

Upload how ever many pictures you want and our program will identify the best faces in each image and put them all onto the image that you identify.

# Setup
Install requirements
```
$ pip install -r requirements.txt
```
# Using the program
```
$ py main.py
```
Upon running the program, your file explorer will pop up allowing you select multiple images.

After selecting your images, you'll be asked to choose which one you want as the "scene" aka the image where all the faces will be placed onto. From there select the file name and you'll have our desired output image.

# See facial points using your webcam
```
$ py webcam.py
```
This handy command will open your webcam and plot the 68 facial features onto your face showing exactly how computers interpret faces.

# Design

Our program reads in the images, identifies all the faces within the image and puts them into face sets. Each face set corresponds to each person across the images. Within the face set we identify the "best face" i.e. the face with the best smile.

After identifying the best faces, we send the chosen scene and a list of the best images to the Aggregate class which will swap all of the faces onto the scene.
