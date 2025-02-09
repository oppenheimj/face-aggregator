#! /usr/bin/env python
import os
import cv2
import argparse
from log import log

from FaceSwap.face_detection import give_face
from FaceSwap.face_swap import face_swap



class Aggregate:

    def __init__(self, batch, dest_img, faces: list):
        # faces should be a list of Face objects
        self.batch = batch
        self.faces = faces
        self.dest_img = dest_img
        self.intermediary_img = self.dest_img.image.copy()

    def swapOneFace(self, face):
        # will find the face in the faceset and then identify that same face in the destination image and morph it into the images
        image_copy = self.intermediary_img.copy()
        # the intersection the faceset of variable face and the faces in self.dest_img should be the face that will be replaced
        face_to_replace = set(self.dest_img.faces).intersection(set(face.faceSet.faces))
        log.info(f"Face {face_to_replace} to replace in destination image")

        src_points, src_shape, src_face = give_face(face.parentImage.image, face)
        # Select dst face
        dst_points, dst_shape, dst_face = give_face(image_copy, list(face_to_replace)[0])

        if src_points is None or dst_points is None:
            log.warn('No face given')
            exit(-1)

        output = face_swap(src_face, dst_face, src_points, dst_points, dst_shape, image_copy)

        self.intermediary_img = output.copy()

    def swapAllFaces(self, out_path="scene.jpg"):
        for face in self.faces:
            log.info(f"Taking this face {face} and putting it on destination image:")
            self.swapOneFace(face)

        cv2.imwrite(os.path.join(os.getcwd(), "files", out_path), self.intermediary_img)
        log.info(f"Output image found at: {out_path}")
