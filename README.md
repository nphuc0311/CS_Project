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

## Usage

```
python main.py
