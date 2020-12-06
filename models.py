import dlib, cv2

MODELS_PATH = 'files/models/'
predictor = dlib.shape_predictor(f'{MODELS_PATH}shape_predictor_68_face_landmarks.dat')
detector = dlib.get_frontal_face_detector()

modelFile = f'{MODELS_PATH}opencv_face_detector_uint8.pb'
configFile = f'{MODELS_PATH}opencv_face_detector.pbtxt'
net = cv2.dnn.readNetFromTensorflow(modelFile, configFile)