# 
Please note that git and python3 are requirements to install and run the detector.
## Setup
### 1. Clone the repository
```shell
git clone https://github.com/panthibivek/Ring_Detection.git
```
### 2. CD into the repository
```shell
cd ring_detection/
```
### 3. Install all the requirements
```shell
pip install -r yolov5/requirements.txt
```

## Example Usage

### With image
![alt text](https://github.com/panthibivek/Ring_Detection/blob/master/test_img.jpg?raw=true)
### With webcam
https://drive.google.com/file/d/1oM8kOnQE9u-03H4Vlgr723bSFe5ecNfX/view?usp=sharing

### To use the detector with image size 640 and confidence 0.6 in webcam
```shell
python3 yolov5/detect.py --weights yolov5/runs/train/exp/weights/best.pt --img 640 --conf 0.4 --source 0
```

# Theory

## Distance estimation
### Distance from Camera
<b> Case I</b> (If bounding-box’s height in pixel is known at a known distance): <br>
Focal length = (known_pixel_height * known_distance) / known_height<br>
Distance = (known_height * focal_length) / pixel_height_now<br>
<b> Case II</b> (If no prior information):<br>
Assumption : When the object is at distance zero, either bbox’s height or width is equal
to the whole frame’s height or width.<br>
Distance
= frame_size / max{pixel_height_now, pixel_width_now}<br>
### Distance from Center of image frame
Euclidean distance

## Pose estimtion
![alt text](https://github.com/panthibivek/Ring_Detection/blob/master/pose_estimation.png?raw=true)


