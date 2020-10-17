import cv2
import dlib

from landmarkPoints import *

class FaceMarker(object):
    def __init__(self, image):
        self.image = image
        self.grayImage = cv2.cvtColor(src=image, code=cv2.COLOR_BGR2GRAY)
        self.predictor = dlib.shape_predictor("files/shape_predictor_68_face_landmarks.dat")

    def detectFaces(self):
        detector = dlib.get_frontal_face_detector()
        self.faces = detector(self.grayImage)

    def identifyFeatures(self, landmarkPoints=landmarkPoints['all'], box=False):
        for face in self.faces:
            if box:
                self.drawBox(face)

            if landmarkPoints:
                self.drawLandmarks(face, landmarkPoints)

        cv2.imshow(winname=f'Face{"s" if len(self.faces) > 1 else ""}', mat=self.image)
        cv2.waitKey(delay=0)
        cv2.destroyAllWindows()

    def drawBox(self, face):
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()

        cv2.rectangle(img=self.image, pt1=(x1, y1), pt2=(x2, y2), color=(0, 255, 0), thickness=4)

    def drawLandmarks(self, face, landmarkPoints):
        landmarks = self.predictor(image=self.grayImage, box=face)

        for p in landmarkPoints:
            x = landmarks.part(p).x
            y = landmarks.part(p).y

            cv2.circle(img=self.image, center=(x, y), radius=3, color=(0, 255, 0), thickness=-1)