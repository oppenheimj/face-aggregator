import tkinter as tk
from tkinter import filedialog
import cv2
from log import log

from Batch import Batch

class BatchLoader(object):
    def __init__(self):
        pass

    def browse(self):
        root = tk.Tk()
        root.withdraw()

        filePaths = filedialog.askopenfilenames()
        images = [(cv2.imread(path), path) for path in filePaths]
        # log.info(f"Images and paths being sent to Batch {images}")

        return Batch(images)
