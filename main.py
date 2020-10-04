# https://towardsdatascience.com/detecting-face-features-with-python-30385aee4a8e
import cv2

img = cv2.imread("files/a.jpg")

cv2.imshow(winname="Face", mat=img)

# Wait for a key press to exit
cv2.waitKey(delay=0)

# Close all windows
cv2.destroyAllWindows()