import cv2
import logging as log

from BatchLoader import BatchLoader

log.basicConfig(level=log.INFO)

batch = BatchLoader().browse()
batch.detectFaces()
batch.generateFaceSets()
batch.draw()