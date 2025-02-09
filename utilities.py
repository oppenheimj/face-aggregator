import cv2

scaleImage = lambda image, scale: cv2.resize(image, (int(image.shape[1]*scale), int(image.shape[0]*scale)))

genList = lambda start, stop: [i for i in range(start, stop+1)]

landmarkPoints = {
    'jaw': genList(0, 16),
    'rightBrow': genList(17, 21),
    'leftBrow': genList(22, 26),
    'nose': genList(27, 35),
    'rightEye': genList(36, 41),
    'leftEye': genList(42, 47),
    'mouth': genList(48, 60),
    'lips': genList(61, 67),
    'all': genList(0, 67)
}

TWENTY_PERCENT = 0.2
