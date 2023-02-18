# 
Please note that python3 is a requirement to run the detector.
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

## Example Usage with webcam
With image size 640 and confidence 0.6 <br>
```shell
python3 yolov5/detect.py --weights yolov5/runs/train/exp/weights/best.pt --img 640 --conf 0.4 --source 0
```
