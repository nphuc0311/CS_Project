import cv2
import dlib
from ultis import *

if __name__ == "__main__":
  cap = cv2.VideoCapture(0)

  # Loading face detector
  detector = dlib.get_frontal_face_detector()
  predictor = dlib.shape_predictor("pretrain/shape_predictor_68_face_landmarks.dat")
  while 1:
    ret, frame = cap.read()
    if ret:
      
    #   frame = phuc_effect(detector, predictor, frame)
    #   frame = phat_effect(detector, predictor, frame)
    #   frame = nam_effect(detector, predictor, frame)

      cv2.imshow('frame',frame)
      if cv2.waitKey(1) & 0xFF == ord('q'):
          break

  # When everything done, release the capture
  cap.release()
  cv2.destroyAllWindows()
