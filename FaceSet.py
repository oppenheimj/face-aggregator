import numpy as np
from log import log

class FaceSet(object):
    def __init__(self):
        self.faces = []
        self.happiest = None

    def addFace(self, face):
        log.info(f'Adding face with center {face.center} to faceSet {id(self)}')
        self.faces.append(face)
        face.setFaceSet(self)
        self.computeCenter()

    def identifyHappiestFace(self):
        score2Face = {face.getSmileScore(): face for face in self.faces}
        bestScore = sorted(list(score2Face))[0]

        self.happiest = score2Face[bestScore]

        log.info(f'Happiest face {id(self.happiest)} with score {bestScore} from image {id(self.happiest.parentImage)}')

    def computeCenter(self):
        xSum = 0
        ySum = 0

        for face in self.faces:
            xSum += face.center.x
            ySum += face.center.y

        self.center = (xSum/len(self.faces), ySum/len(self.faces))

    def computeDistanceFrom(self, point):
        return np.sqrt((self.center[0]-point.x)**2 + (self.center[1]-point.y)**2)
