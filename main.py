import cv2

from log import log
from BatchLoader import BatchLoader
from Aggregate import Aggregate

batch = BatchLoader().browse()
batch.detectFaces()
batch.generateFaceSets()
faceSets = batch.getFaceSets()
ag = Aggregate(batch, batch.images[0], batch.images[1].getFaces())
# put onto a.jpg, the girl's face from b.jpg
ag.swapAllFaces("test.jpg")
# batch.draw()


# batch.identifyHappiestFaces()
# At this point, every faceSet in the batch knows the best face
# and from what image it originated. All that's left to do is
# swap!

# batch.draw()
