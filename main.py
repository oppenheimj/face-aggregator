import cv2

from log import log
from BatchLoader import BatchLoader
from Aggregate import Aggregate

batchLoader = BatchLoader() # created its own object so we can check if enough images were uploaded
batch = batchLoader.browse()
batch.detectFaces()
batch.generateFaceSets()
faceSets = batch.getFaceSets()
batch.identifyHappiestFaces()

# Create Aggregate class to add the best faces onto the chosen image
ag = Aggregate(batch, batch.getUserScene(), batch.getHappiestFaces())


output_path = input("Type desired file name (no extension) or press Enter to use default file name: ")
if len(output_path) > 0:
    ag.swapAllFaces(output_path + ".jpg")
else:
    ag.swapAllFaces("best_image.jpg")
