import cv2
import dlib
from ultis import *
from tkinter import *


if __name__ == "__main__":
    cap = cv2.VideoCapture(0)

    # Loading face detector
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("pretrain/shape_predictor_68_face_landmarks.dat")

    gif_to_numpy("gif/glow_mini.gif")

    window = Tk() #call tkinter function to create a tkinter window // create GUI window // window is the named given to the GUI: name is needed for attributes
    window.title("App") #Title of the Message Window // Will appear on the Top // title widget
    window.geometry('475x75') #Defines the width, height and coordinates of the top left corner of the frame as below in pixels | (width x height + XPOS + YPOS) //geometry widget
    window.configure(bg='#000000', highlightbackground='#000000') 

    def one():
        frame_count = 0
        while 1:
            ret, frame = cap.read()
            if ret:
                # frame = Son_Goku(detector, predictor, frame, frame_count)
                frame_count += 1
                cv2.imshow('frame',frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        cv2.destroyAllWindows()


    def two():
        while 1:
            ret, frame = cap.read()
            if ret:
                frame = Anbu(detector, predictor, frame)
                cv2.imshow('frame',frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        cv2.destroyAllWindows()


    def three():
        temp = 0
        while 1:
            ret, frame = cap.read()
            if ret:
                frame = Sharingan(detector, predictor, frame, temp)
                temp += 1
                if temp >= T:
                    temp = 0
                cv2.imshow('frame',frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        cv2.destroyAllWindows()

    button_1 = Button(window, text='Goku - SuperSaiyan', command=one, fg='black', bg='yellow', height=3, width=20, padx=5, pady=5).pack(side=LEFT) 
    button_2 = Button(window, text='ANBU', command=two, fg='black', bg='white', height=3, width=20, padx=5, pady=5).pack(side=LEFT) 
    button_3 = Button(window, text='Sharingan', command=three, fg='black', bg='red', height=3, width=20, padx=5, pady=5).pack(side=LEFT) 


    window.mainloop() 

            



