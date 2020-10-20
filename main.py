import cv2

from FaceMarker import FaceMarker
from landmarkPoints import *
from sceneIntake import Scene


######### Individual testing below

# a = cv2.imread("files/a.jpg")
# b = cv2.imread("files/b.jpg")
#
# faceMarker_a = FaceMarker(a)
# faceMarker_b = FaceMarker(b)
#
# # faceMarker.detectFaces() # removed this because I included it in the __init__ of FaceMarker
# for landmark in landmarkPoints.keys():
#     print(landmark)
#     faceMarker_a.test(landmarkPoints[landmark])
#     faceMarker_b.test(landmarkPoints[landmark])

# faceMarker_a.identifyFeatures(landmarkPoints['all'], box=True)
# faceMarker_b.identifyFeatures(landmarkPoints['all'], box=True)

########### Using Scene class below

s = Scene(["files/a.jpg","files/b.jpg"])
