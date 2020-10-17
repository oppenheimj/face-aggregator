import cv2

from FaceMarker import FaceMarker
from landmarkPoints import *

image = cv2.imread("files/a.jpg")

faceMarker = FaceMarker(image)

faceMarker.detectFaces()
faceMarker.identifyFeatures(landmarkPoints['jaw'], box=True)