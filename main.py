import cv2
import dlib
from ultis import *



print(T)
if __name__ == "__main__":
    cap = cv2.VideoCapture(0)

    # Loading face detector
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("pretrain/shape_predictor_68_face_landmarks.dat")

    frame_count = 0
    temp = 0

    while 1:
        
        ret, frame = cap.read()
        if ret:
            # frame = phuc_effect(detector, predictor, frame, frame_count)

            frame_count += 1
            frame = phat_effect(detector, predictor, frame, temp)
            temp += 1
            if temp >= T:
                temp = 0
            frame = nam_effect(detector, predictor, frame)
            cv2.imshow('frame',frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                
                break
    cap.release()
    cv2.destroyAllWindows()
            
  
 

    # When everything done, release the capture
