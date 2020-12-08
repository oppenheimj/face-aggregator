import dlib, cv2
import numpy as np

from utilities import landmarkPoints
from log import log

MODELS_PATH = 'files/models/'

def detectLandmarks(image, box):
    predictor = dlib.shape_predictor(f'{MODELS_PATH}shape_predictor_68_face_landmarks.dat')
    landmarks = predictor(image=image, box=box)

    return [(landmarks.part(pt).x, landmarks.part(pt).y) for pt in landmarkPoints['all']]

def detectFaceBoxes(Image, confThreshold):
    modelFile = f'{MODELS_PATH}opencv_face_detector_uint8.pb'
    configFile = f'{MODELS_PATH}opencv_face_detector.pbtxt'
    net = cv2.dnn.readNetFromTensorflow(modelFile, configFile)

    blob = cv2.dnn.blobFromImage(Image.image)
    net.setInput(blob)
    detections = net.forward()

    faceMask = detections[0, 0, :, 2] > confThreshold
    numFaces = np.count_nonzero(faceMask)
    log.info(f'{Image.fileName}: Detected {numFaces} faces with confidence > {confThreshold}%')

    return [_detectionToBox(Image.image, face) for face in detections[0, 0, faceMask]]

def _detectionToBox(image, detection):
    frameHeight, frameWidth, _ = image.shape

    x1 = int(detection[3] * frameWidth)
    y1 = int(detection[4] * frameHeight)
    x2 = int(detection[5] * frameWidth)
    y2 = int(detection[6] * frameHeight)

    return dlib.rectangle(left=x1, top=y1, right=x2, bottom=y2)
