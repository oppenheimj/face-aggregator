import os, cv2, math

from Image import Image
from FaceSet import FaceSet
from utilities import TWENTY_PERCENT
from log import log

class Batch(object):
    def __init__(self, images_paths):
        # TODO: Intelligently scale images using smallest dimension
        self.images = [Image(self, image, path, 0.2) for image, path in images_paths]

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

    def identifyHappiestFaces(self):
        for faceSet in self.faceSets:
            faceSet.identifyHappiestFace()

    def getHappiestFaces(self):
        return [faceSet.happiest for faceSet in self.faceSets]

    def getUserScene(self):
        # Get the image paths
        images_paths = {i: (image, image.path) for i, image in enumerate(self.images)}
        print()
        for key, (image, path) in images_paths.items():
            print(f"{key}: {path[path.rfind('/')+1:]}")
        try:
            chosen_image_index = int(input("Please type in the number corresponding to the image you want all the faces to end up on:\n"))
        except ValueError:
            chosen_image_index = -1
            print("That was not an integer")
        while not 0 <= chosen_image_index < len(self):
            try:
                chosen_image_index = int(input("Choose only one of the numbers on the terminal:\n"))
            except ValueError:
                chosen_image_index = -1
                print("That was not an integer")
        return images_paths[chosen_image_index][0]

    def draw(self):
        for image in self.images:
            image.draw()

    def getFaceSets(self):
        return self.faceSets

    def __len__(self):
        return len(self.images)
