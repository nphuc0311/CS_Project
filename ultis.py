
from __future__ import print_function
import gif2numpy
import numpy as np
import cv2
import dlib
from math import hypot
import imageio


gif = np.load('./gif/eyes1.npy')
gif1 = np.load('./gif/eyes.npy')
index = 0
index1 = 0
T = len(gif) + len(gif1) + 27
def gif_to_numpy(path):
    frames, _, _ = gif2numpy.convert(path)
    sprites=np.array(frames)
    np.save("gif/effect3.npy", sprites)

    # frames = imageio.mimread(imageio.core.urlopen("https://i.gifer.com/FOUL.gif").read(), '.gif')
    # sprites = [frame[...,0:3] for frame in frames]
    # sprites=np.array(sprites)
    # # print(len(sprites))
    # np.save("eyes.npy", sprites)

def merge(frame, hair, mask, centre):

    frows, fcols, _ = frame.shape
    hrows, hcols, _ = hair.shape
    
    x, y = (centre[0] - hcols//2, centre[1] - hrows//2)
    
    frame_roi = frame[ y:y+hrows, x:x+hcols ,... ]

    if frame_roi.shape == hair.shape:  
        np.copyto(frame_roi, hair,where=mask[...,np.newaxis]>0)


# Add glow overlay image
def add_glow(frame, glow, origin):
    
    frows, fcols, _ = frame.shape
    grows, gcols, _ = glow.shape
    
    x, y = origin

    frame_roi = frame[ y:y+grows, x:x+gcols ,... ]
    
    # Check bounds and overlay aura glow
    if frame_roi.shape ==  glow.shape:
        glow_roi = cv2.addWeighted(frame_roi,1.0, glow,0.95,0)
        np.copyto(frame_roi, glow_roi)

# Check if mouth is open
def mouth_open(landmarks):
    
    l1 =   landmarks.part(50).y - landmarks.part(61).y
    l2 =   landmarks.part(51).y - landmarks.part(62).y
    l3 =  landmarks.part(52).y - landmarks.part(63).y
    
    m1 =  landmarks.part(61).y - landmarks.part(67).y
    m2 =  landmarks.part(62).y - landmarks.part(66).y
    m3 =  landmarks.part(63).y - landmarks.part(65).y

    # m1 =  landmarks.part(50).y - landmarks.part(58).y
    # m2 =  landmarks.part(51).y - landmarks.part(57).y
    # m3 =  landmarks.part(52).y - landmarks.part(56).y    

    # Calculate average mouth and lip heights
    lip_height = abs((l1+l2+l3)//3)
    mouth_height = abs((m1+m2+m3)//3)

    # print(mouth_height, lip_height)
    
    if (mouth_height > lip_height):
       # mouth is open
       return True
    else:
       # mouth is closed
       return False

def Son_Goku(detector, predictor, frame, frame_count):
    # Load custom hair image with alpha mask
    hair_image = cv2.imread("images/ssj_hair.png")
    hair_mask = cv2.imread("images/ssj_hair.png", cv2.IMREAD_UNCHANGED)[...,3]

    # Load golden aura sprite images (animation)
    glow_imgs = np.load('gif/effect3.npy')
    # print(len(glow_imgs))
    glow_imgs_2 = np.load('gif/effect_2.npy')

    # Load black hair image with alpha mask
    black_hair = cv2.imread("images/black_hair.png")
    black_hair_mask = cv2.imread("images/black_hair.png", cv2.IMREAD_UNCHANGED)[...,3]

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces from the grayscale image
    faces = detector(gray)
    # show = np.copy(frame[227:330, 238:342,:])
    # cv2.imshow('bounding box', show)
    # cv2.waitKey(1)
    # # cv2.destroyAllWindows()
    # # print(faces)
    
    if len(faces) == 1:

        # Predict facial landmark points on the frame
        landmarks = predictor(gray, faces[0])

        # Find the extreme landmark points
        left_face = (landmarks.part(0).x, landmarks.part(0).y)
        right_face = (landmarks.part(16).x, landmarks.part(16).y)


        # Choose yellow hair if mouth is open
        if (mouth_open(landmarks)):
            hair_im = hair_image
            hair_mk = hair_mask
            hwidth_multiplier = 2
            htop_multiplier = 100
            ssj = True

        else:
            hair_im = black_hair
            hair_mk = black_hair_mask
            hwidth_multiplier = 2.6
            htop_multiplier = 100
            ssj = False           

        # Configure hair width and height
        hair_width = int(hypot(left_face[0] - right_face[0],
                        left_face[1] - right_face[1])*hwidth_multiplier)
        # print(left_face[1] - right_face[1])
        hair_height = int(hair_width)

        # Resize hair and mask
        hair =  cv2.resize(hair_im, (hair_width, hair_height))
        mask =  cv2.resize(hair_mk, (hair_width, hair_height), interpolation = cv2.INTER_NEAREST)

        # Compute hair location
        hair_x = landmarks.part(27).x
        hair_y = int(landmarks.part(27).y - htop_multiplier)

        merge(frame, hair, mask, (hair_x, hair_y))
        # add_glow(frame, glow, (glow_x_left , glow_y_top))

        # Resize the aura image frame
        glow =  cv2.resize(glow_imgs[frame_count%int(len(glow_imgs))], (int(hair_width*2.4), int(hair_width*3.4) ))
        glow_2 = cv2.resize(glow_imgs_2[frame_count%int(len(glow_imgs_2))], (int(hair_width*2.4), int(hair_width*3.4) ))

        # Compute the hair location
        glow_x_left = landmarks.part(27).x - int(hair_width * 1.2)
        glow_y_top = int(landmarks.part(27).y  + (landmarks.part(27).y - landmarks.part(30).y )*7)
        
        # Crop the aura image based on height 
        glow = glow[0:frame.shape[0]-glow_y_top, ...]
        glow_2 = glow_2[0:frame.shape[0]-glow_y_top, ...]
        if ssj:
            add_glow(frame, glow, (glow_x_left , glow_y_top))
            add_glow(frame, glow_2, (glow_x_left , glow_y_top))


    return frame


def Sharingan(detector, predictor, frame, frame_count):
    global index, index1, eyes_image, eyes_mask

    if frame_count >= 0:
        eyes_image = cv2.cvtColor(gif[index], cv2.COLOR_BGR2RGB)
        eyes_mask = cv2.cvtColor(eyes_image,cv2.COLOR_BGR2GRAY)

        index += 1
        if index == len(gif) - 3:
            index = 0


    if frame_count >= len(gif) - 3:
        eyes_image = cv2.cvtColor(gif1[index1], cv2.COLOR_BGR2RGB)
        eyes_mask = cv2.cvtColor(eyes_image,cv2.COLOR_BGR2GRAY)
    
        index1 += 1
        if index1 == len(gif1):
            index1 = 0

        
    if frame_count >= len(gif) + len(gif1):
        eyes_image = cv2.imread("images/rinnergan.png")
        eyes_mask = cv2.imread("images/rinnergan.png", 0)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces from the grayscale image
    faces = detector(gray)

    if len(faces) == 1:
        landmarks = predictor(gray, faces[0])
        
       
    
        # Left eyes
        left_point = (landmarks.part(37).x, landmarks.part(37).y)
        right_point = (landmarks.part(40).x, landmarks.part(40).y)

        eyes_width = abs(left_point[0]-right_point[0])*2
        eyes_height = int(eyes_width*frame.shape[0]/frame.shape[1])

        eyes = cv2.resize(eyes_image, (eyes_width, eyes_height))
        mask =  cv2.resize(eyes_mask, (eyes_width, eyes_height), interpolation = cv2.INTER_NEAREST)

        eyes_x = int(landmarks.part(37).x + abs((landmarks.part(38).x - landmarks.part(37).x)//2))
        eyes_y = abs(landmarks.part(38).y)

        merge(frame, eyes, mask, (eyes_x, eyes_y))

        # Right eyes
        left_point = (landmarks.part(43).x, landmarks.part(43).y)
        right_point = (landmarks.part(46).x, landmarks.part(46).y)

        eyes_width = abs(left_point[0]-right_point[0])*2
        eyes_height = int(eyes_width*frame.shape[0]/frame.shape[1])

        eyes = cv2.resize(eyes_image, (eyes_width, eyes_height))
        mask =  cv2.resize(eyes_mask, (eyes_width, eyes_height), interpolation = cv2.INTER_NEAREST)

        eyes_x = int(landmarks.part(43).x + abs((landmarks.part(43).x - landmarks.part(44).x)//2))
        eyes_y = abs(landmarks.part(44).y)

 
        # print(eyes_width, eyes_height)

        merge(frame, eyes, mask, (eyes_x, eyes_y))


    return frame



def Anbu(detector, predictor, frame):
   
    # Load custom hair image with alpha mask
    mask_image = cv2.imread("images/anbu.png")
    mask_mask = cv2.imread("images/anbu.png", cv2.IMREAD_UNCHANGED)[...,3]

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces from the grayscale image
    faces = detector(gray)

    if len(faces) == 1:
        landmarks = predictor(gray, faces[0])

        # Left eyes
        left_point = (landmarks.part(1).x, landmarks.part(1).y)
        right_point = (landmarks.part(15).x, landmarks.part(15).y)

        hair_width = int(hypot(left_point[0] - right_point[0],
                        left_point[1] - right_point[1])*1.5)
        hair_height = int(hair_width*1.1)

        # Resize hair and mask
        mmask =  cv2.resize(mask_image, (hair_width, hair_height))
        mask =  cv2.resize(mask_mask, (hair_width, hair_height), interpolation = cv2.INTER_NEAREST)

        eyes_x = int(landmarks.part(27).x)
        eyes_y = abs(landmarks.part(27).y)

        merge(frame, mmask, mask, (eyes_x, eyes_y))

    return frame
