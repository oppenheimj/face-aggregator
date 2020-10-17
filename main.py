import cv2

from FaceMarker import FaceMarker

image = cv2.imread("files/a.jpg")

faceMarker = FaceMarker(image)

faceMarker.detectFaces()
faceMarker.identifyFeatures()