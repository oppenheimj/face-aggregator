import cv2

from log import log
from BatchLoader import BatchLoader
from Aggregate import Aggregate

batchLoader = BatchLoader() # created its own object so we can check if enough images were uploaded
batch = batchLoader.browse()
while len(batch) <= 1:
    log.warn("Not enough images were uploaded to aggregate faces. Please try again")
    batch = batchLoader.browse()
batch.detectFaces()
batch.generateFaceSets()
faceSets = batch.getFaceSets()
batch.identifyHappiestFaces()
bestFaces = [faceSet.happiest for faceSet in batch.faceSets]

# Get the image paths
images_paths = {i: (image, image.path) for i, image in enumerate(batch.images)}
print()
for key, (image, path) in images_paths.items():
    print(f"{key}: {path[path.rfind('/')+1:]}")
try:
    chosen_image_index = int(input("Please type in the number corresponding to the image you want all the faces to end up on:\n"))
except ValueError:
    chosen_image_index = -1
    print("That was not an integer")
while not 0 <= chosen_image_index < len(batch.images):
    try:
        chosen_image_index = int(input("Choose only one of the numbers on the terminal:\n"))
    except ValueError:
        chosen_image_index = -1
        print("That was not an integer")

# Create Aggregate class to add the best faces onto the chosen image
ag = Aggregate(batch, images_paths[chosen_image_index][0], bestFaces)


output_path = input("Type desired file name (no extension) or press Enter to use default file name: ")
if len(output_path) > 0:
    ag.swapAllFaces(output_path + ".jpg")
else:
    ag.swapAllFaces("lin_test.jpg")
