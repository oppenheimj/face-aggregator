import os, cv2, math

from Image import Image
from FaceSet import FaceSet
from utilities import TWENTY_PERCENT

class Batch(object):
    def __init__(self, images):
        self.images = [Image(self, image, TWENTY_PERCENT) for image in images]

    def detectFaces(self):
        for image in self.images:
            image.detectFaces()

    def generateFaceSets(self):
        self.faceSets = []

        for i, image in enumerate(self.images):
            for face in image.faces:
                if i == 0:
                    faceSet = FaceSet()
                    faceSet.addFace(face)
                    self.faceSets.append(faceSet)
                else:
                    faceSetIndex = 0
                    shortestDistance = math.inf

                    for j, faceSet in enumerate(self.faceSets):
                        distance = faceSet.computeDistanceFrom(face.center)
                        if distance < shortestDistance:
                            faceSetIndex = j
                            shortestDistance = distance

                    self.faceSets[faceSetIndex].addFace(face)

    def draw(self):
        for image in self.images:
            image.draw()

    def getFaceSets(self):
        return self.faceSets
