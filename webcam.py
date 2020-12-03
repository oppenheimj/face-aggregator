import cv2

from Image import Image

# read the image
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    image = Image(None, frame)
    image.detectFaces()
    image.draw()

    # Exit when escape is pressed
    if cv2.waitKey(delay=1) == 27:
        break

# When everything done, release the video capture and video write objects
cap.release()

# Close all windows
cv2.destroyAllWindows()