import cv2
import math
from log import log
import numpy as np

from utilities import scaleImage, landmarkPoints
from models import predictor, detector, net
import dlib
from Face import Face

class Image(object):
    def __init__(self, batch, image, path, scale=0):
        self.batch = batch
        self.image = scaleImage(image, scale) if scale else image
        self.grayImage = cv2.cvtColor(src=self.image, code=cv2.COLOR_BGR2GRAY)
        self.path = path

    def getFaces(self):
        return self.faces

    def detectFacesOld(self):
        print('OLD DETECT FACES')
        self.faces = []

        for box in detector(self.grayImage):
            landmarks = predictor(image=self.grayImage, box=box)
            landmarkPts = [(landmarks.part(pt).x, landmarks.part(pt).y) for pt in landmarkPoints['all']]
            self.faces.append(Face(self, box, landmarkPts))

        log.info(f"Number of faces in image: {len(self.faces)}")

    def detectFaces(self):
        # self.detectFacesOld()
        self.detectFacesNew()

    def detectFacesNew(self):
        self.faces = []

        frameHeight, frameWidth = self.grayImage.shape

        # self.detectFacesOld()
        print('NEW DETECT FACES')

        blob = cv2.dnn.blobFromImage(self.image)
        net.setInput(blob)
        detections = net.forward()

        conf_threshold=0.5

        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > conf_threshold:
                x1 = int(detections[0, 0, i, 3] * frameWidth)
                y1 = int(detections[0, 0, i, 4] * frameHeight)
                x2 = int(detections[0, 0, i, 5] * frameWidth)
                y2 = int(detections[0, 0, i, 6] * frameHeight)
                box = dlib.rectangle(left=x1, top=y1, right=x2, bottom=y2)
                landmarks = predictor(image=self.grayImage, box=box)
                landmarkPts = [(landmarks.part(pt).x, landmarks.part(pt).y) for pt in landmarkPoints['all']]
                self.faces.append(Face(self, box, landmarkPts))

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

    # ehhhh maybe we shouldn't use this
    def getLandmarksValue(self, face, landmarkPoints):
        """
        Given the image, the faces, and the landmarkPoints, this function will return a tuple of 68 values. Each value being the difference between the current point and the one before it. Each person ~*~should~*~ then have a unique set of values so that we can identify them automatically

        Returns a 68-index tuple of values per face

        TODO: Can also look at the face boundaries and see where they start and end to help identify the face
        """
        landmarks = predictor(image=self.grayImage, box=face)
        differences = []
        print(face)
        for point in range(len(landmarkPoints)):
            if point == 0:
                x_now, x_before = landmarks.part(landmarkPoints[point]).x, landmarks.part(landmarkPoints[-1]).x
                y_now, y_before = landmarks.part(landmarkPoints[point]).y, landmarks.part(landmarkPoints[-1]).y
            else:
                x_now, x_before = landmarks.part(landmarkPoints[point]).x, landmarks.part(landmarkPoints[point-1]).x
                y_now, y_before = landmarks.part(landmarkPoints[point]).y, landmarks.part(landmarkPoints[point-1]).y
            distance = math.sqrt((x_now-x_before)**2 + (y_now-y_before)**2)
            differences.append(distance)
        return differences

    def getFaceAreas(self, face, landmarkPoints):
        landmarks = predictor(image=self.grayImage, box=face)

        x, y = list(), list()
        for point in landmarkPoints:
            x.append(landmarks.part(point).x)
            y.append(landmarks.part(point).y)

        x, y = np.asarray(x), np.asarray(y)
        # https://stackoverflow.com/questions/24467972/calculate-area-of-polygon-given-x-y-coordinates
        area = 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))
        return area
