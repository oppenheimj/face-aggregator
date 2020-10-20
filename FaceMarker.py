import cv2, dlib, math
import numpy as np
from landmarkPoints import *


class FaceMarker(object):
    def __init__(self, image, resize=False):
        if resize:
            image_scale = .5
            self.image = cv2.resize(image, (int(image.shape[1]*image_scale), int(image.shape[0]*image_scale)))
        else:
            self.image = image
        self.grayImage = cv2.cvtColor(src=self.image, code=cv2.COLOR_BGR2GRAY)
        self.predictor = dlib.shape_predictor("files/shape_predictor_68_face_landmarks.dat")
        self.faces = self.detectFaces()
        self.landmarks = self.defineLandmarks()

    def getFaces(self):
        return self.faces

    def defineLandmarks(self):
        l = dict()
        for face in self.faces:
            landmarks = self.predictor(image=self.grayImage, box=face)
            temp = []
            for point in landmarkPoints['all']:
                temp.append((landmarks.part(point).x, landmarks.part(point).y))
            l[face] = temp
        return l

    def getLandmarks(self):
        return self.landmarks

    def detectFaces(self):
        detector = dlib.get_frontal_face_detector()
        faces = detector(self.grayImage)

        #### remove these lines after- just for testing
        # print("Number of faces detected: {}".format(len(faces)))
        # for i, d in enumerate(faces):
        #     print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
        #         i, d.left(), d.top(), d.right(), d.bottom()))
        ####
        return faces

    def identifyFeatures(self, landmarkPoints=[], box=False):
        for face in self.faces:
            if box:
                self.drawBox(face)

            if landmarkPoints:
                self.drawLandmarks(face, landmarkPoints)

        cv2.imshow(winname=f'Face{"s" if len(self.faces) > 1 else ""}', mat=self.image) # added the resize because I could only see a quarter of the image on my computer
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



            # ehhhh maybe we shouldn't use this
    def getLandmarksValue(self, face, landmarkPoints):
        """
        Given the image, the faces, and the landmarkPoints, this function will return a tuple of 68 values. Each value being the difference between the current point and the one before it. Each person ~*~should~*~ then have a unique set of values so that we can identify them automatically

        Returns a 68-index tuple of values per face

        TODO: Can also look at the face boundaries and see where they start and end to help identify the face
        """
        landmarks = self.predictor(image=self.grayImage, box=face)
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
        landmarks = self.predictor(image=self.grayImage, box=face)

        x, y = list(), list()
        for point in landmarkPoints:
            x.append(landmarks.part(point).x)
            y.append(landmarks.part(point).y)

        x, y = np.asarray(x), np.asarray(y)
        # https://stackoverflow.com/questions/24467972/calculate-area-of-polygon-given-x-y-coordinates
        area = 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))
        return area


    def test(self, landmarkPoints):
        for face in self.faces:
            # print(self.getLandmarksValue(face, landmarkPoints))
            print(face, self.getFaceAreas(face, landmarkPoints))
