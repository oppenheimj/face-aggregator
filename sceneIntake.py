import tkinter as tk
from tkinter import filedialog
import os, cv2, math
from FaceMarker import FaceMarker


class Scene:

    def __init__(self, images=None):
        """
        images is a list/tuple of image names including file extension
        """
        if not images:
            self.images = self.getFiles()
        else:
            self.images = images
        self.faces = self.createFaceDict()

    def getFiles(self):
        root = tk.Tk()
        root.withdraw()

        file_path = filedialog.askopenfilenames()
        return file_path

    def createFaceDict(self):
        """
        This will go through all the images, identify the faces and then match up the faces in each picture to the corresponding person

        Result will be a dictionary with keys as face_n and values as a list of tuples of face boundary coordinates
        """
        # facemarkers = list()
        # all_faces_rects = dict()
        face_centers = dict()
        centers_to_rect = dict()
        for image in self.images:
            faces = FaceMarker(cv2.imread(image)).getFaces()
            # faces = marker.getFaces()
            # all_faces_rects[image] = faces
            face_centers_list = list()
            for face in faces:
                face_centers_list.append(face.center())
                centers_to_rect[face.center()] = face
            face_centers[image] = face_centers_list
            # facemarkers.append(marker)



        # Goes through the centers and does euclidian distance from that center to all other centers
        # if the distance < threshold then we say the faces correspond. Add to the dict according to that face
        threshold = 150
        faces = dict()
        i = 0

        for face in face_centers[self.images[0]]:
            faces[i] = []
            for other_face in centers_to_rect.keys():
                if math.sqrt((face.x-other_face.x)**2 + (face.y-other_face.y)**2) < threshold: # we'll have to review this number
                    faces[i].append(centers_to_rect[other_face])
            i += 1

        return faces



if __name__ == '__main__':
    s = Scene()
