from log import log
from BatchLoader import BatchLoader
from Aggregate import Aggregate

import sys

args = sys.argv

batchLoader = BatchLoader()
batch = batchLoader.browse()

batch.detectFaces()
batch.generateFaceSets()
batch.identifyHappiestFaces()

if 'draw' in args:
    batch.draw()
else:
    # Create Aggregate class to add the best faces onto the chosen image
    ag = Aggregate(batch, batch.getUserScene(), batch.getHappiestFaces())

    output_path = input("Type desired file name (no extension) or press Enter to use default file name: ")
    ag.swapAllFaces(f'{output_path if len(output_path) else "best_image"}.jpg')
