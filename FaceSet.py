import numpy as np
from log import log

class FaceSet(object):
    def __init__(self):
        self.faces = []

    def addFace(self, face):
        log.info(f'Adding face with center {face.center} to faceSet {self}')
        self.faces.append(face)
        face.setFaceSet(self)
        self.computeCenter()

    def computeCenter(self):
        xSum = 0
        ySum = 0

        for face in self.faces:
            xSum += face.center.x
            ySum += face.center.y

        self.center = (xSum/len(self.faces), ySum/len(self.faces))

    def computeDistanceFrom(self, point):
        return np.sqrt((self.center[0]-point.x)**2 + (self.center[1]-point.y)**2)
