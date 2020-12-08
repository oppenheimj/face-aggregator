import dlib, cv2

from utilities import landmarkPoints
from log import log

MODELS_PATH = 'files/models/'

def detectLandmarks(image, box):
    predictor = dlib.shape_predictor(f'{MODELS_PATH}shape_predictor_68_face_landmarks.dat')
    landmarks = predictor(image=image, box=box)

    return [(landmarks.part(pt).x, landmarks.part(pt).y) for pt in landmarkPoints['all']]

def detectFaceBoxes(image, confThreshold):
    modelFile = f'{MODELS_PATH}opencv_face_detector_uint8.pb'
    configFile = f'{MODELS_PATH}opencv_face_detector.pbtxt'
    net = cv2.dnn.readNetFromTensorflow(modelFile, configFile)

    blob = cv2.dnn.blobFromImage(image)
    net.setInput(blob)
    detections = net.forward()

    boxes = []

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        log.info(f'Detected face with confidence {confidence}')

        if confidence > confThreshold:
            boxes.append(_detectionToBox(image, detections[0, 0, i]))

    return boxes

def _detectionToBox(image, detection):
    frameHeight, frameWidth, _ = image.shape

    x1 = int(detection[3] * frameWidth)
    y1 = int(detection[4] * frameHeight)
    x2 = int(detection[5] * frameWidth)
    y2 = int(detection[6] * frameHeight)

    return dlib.rectangle(left=x1, top=y1, right=x2, bottom=y2)
