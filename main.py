import cv2
import logging as log

from BatchLoader import BatchLoader
from Aggregate import Aggregate

log.basicConfig(level=log.INFO)

batch = BatchLoader().browse()
batch.detectFaces()
batch.generateFaceSets()
faceSets = batch.getFaceSets()
ag = Aggregate(batch, batch.images[0], batch.images[1].getFaces())
# put onto a.jpg, the girl's face from b.jpg
ag.swapAllFaces("test.jpg")
# batch.draw()
