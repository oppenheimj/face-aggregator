import cv2
import math
from log import log
import numpy as np

from utilities import scaleImage, landmarkPoints
from models import detectFaceBoxes, detectLandmarks
from Face import Face

import dlib

class Image(object):
    def __init__(self, batch, image, path, scale=0):
        self.batch = batch
        self.image = scaleImage(image, scale) if scale else image
        self.grayImage = cv2.cvtColor(src=self.image, code=cv2.COLOR_BGR2GRAY)
        self.path = path

    def getFaces(self):
        return self.faces

    def detectFaces(self):
        # This confidence threshold can be tuned. 96% seems to work well.
        boxes = detectFaceBoxes(self.image, confThreshold=0.96)
        self.faces = [Face(self, box, detectLandmarks(self.grayImage, box)) for box in boxes]

    def draw(self, webcam=False):
        for face in self.faces:
            if webcam:
                face.getSmileScore()
            face.drawBox()
            face.drawLandmarks()

        cv2.imshow(winname=f'Face{"s" if len(self.faces) > 1 else ""}', mat=self.image)
        if not webcam:
            cv2.waitKey(delay=0)
            cv2.destroyAllWindows()
