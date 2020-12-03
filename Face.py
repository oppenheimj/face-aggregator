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

    def getSmileScore(self):
        '''
        Variables a and b are the left and right corners of the mouth and
        c is the center of the lower lip. Let AB be the line connecting
        a and b. The smile score is the ratio of the length of AB to the
        length of the distance from c to AB.
        '''

        a = self.landmarks[48]
        b = self.landmarks[54]
        c = self.landmarks[47]

        AB_m = (a[1] - b[1]) / (a[0] - b[0])
        AB_b = a[1] - AB_m * a[0]

        c_dist = abs(AB_b + AB_m * c[0] - c[1]) / math.sqrt(1 + AB_m ** 2)
        ab_dist = math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
        score = c_dist / ab_dist

        log.info(f'Face {id(self)} has score {score} using points a {a}; b {b}; c {c}')

        return c_dist / ab_dist

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
