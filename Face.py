import cv2
import math
from log import log

class Face(object):
    def __init__(self, parentImage, box, landmarks):
        self.parentImage = parentImage
        self.boxCorners = {
            'topLeft': (box.left(), box.top()),
            'bottomRight': (box.right(), box.bottom())
        }
        self.box = box
        self.center = box.center()
        self.landmarks = landmarks

    def drawBox(self):
        cv2.rectangle(
            img=self.parentImage.image,
            pt1=self.boxCorners['topLeft'],
            pt2=self.boxCorners['bottomRight'],
            color=(0, 255, 0),
            thickness=4
        )

    def drawLandmarks(self):
        for point in self.landmarks:
            cv2.circle(
                img=self.parentImage.image,
                center=point,
                radius=2,
                color=(0, 255, 0),
                thickness=-1
            )

    def setFaceSet(self, faceSet):
        self.faceSet = faceSet

        # need to add this so we can grab the right face in the destination image to swap out
