# CS Project
## Prerequisites

Install: Dlib and Gif2Numpy
 
```
pip -r requirements.txt
```

## Download 

CNN Dlib Face Detector - [mmod_human_face_detector.dat](http://dlib.net/files/mmod_human_face_detector.dat.bz2)<br />
CNN Dlib face Landmark Detection - [shape_predictor_68_face_landmarks.dat](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2)

## Suggestion
```
├───gif
│       effect_1.gif
│       effect_2.gif
│       effect_3.npy
│       ...
│
├───images
│       image_1.png
│       image_2.png
│       image_3.png
│       ...
│
├───pretrain
│       mmod_human_face_detector.dat
│       shape_predictor_68_face_landmarks.dat
```

## How to code your effect

In **ultis.py**, please code your effect in to function **phat_effect** or **nam_effect**
```
def phat_effect(detector, predictor, frame):
    # Write your code here
    ...
    return frame
    
def nam_effect(detector, predictor, frame):
    # Write your code here
    ...
    return frame
```
Change the **.gif path** if needed in **main.py**
```
gif_to_numpy("path_to_gif")
```
Then **uncomment** your function effect in **main.py**
```
#   frame = phuc_effect(detector, predictor, frame)
#   frame = phat_effect(detector, predictor, frame)
#   frame = nam_effect(detector, predictor, frame)
```
## Run

```
python main.py
<<<<<<< HEAD
```
=======
```
>>>>>>> d0a5b48b00818178da24b4415d90186e09efece1
