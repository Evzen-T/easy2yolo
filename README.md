# **Easy to Yolo**
## **A Easy step by step guide to YoloV5 & YoloV7**
1. Decide on object to detect
2. Dataset Collection
3. Dataset Annotation + Cleaning
4. Training
5. Conversion
6. Inference

---
## **1 - Decide on object to detect**
- Whats the issue at hand?
    1. Security issue
    2. Safety issue
    3. 
- What object are you detecting?
    1. Face (Facial Recognition)
    2. Helmet (Object Detection)
    3. 

## **2 - Dataset Collection**
- What method are you using to collect data?
    1. Camera/Webcam
        - Use takepic.ipynb
    2. Online sources
        - Use Open Images Dataset ([OIDv7](https://storage.googleapis.com/openimages/web/visualizer/index.html)) by google

## **3 - Dataset Annotation + Cleaning**
**Annotation Tools:**

Bounding boxes - Use labelimg ([Github repo](https://github.com/heartexlabs/labelImg))
```bash
#To clone & download lablelimg
git clone https://github.com/heartexlabs/labelImg.git
pip3 install pyqt5 lxml --upgrade
cd labelImg
pyrcc5 -o libs/resources.py resources.qrc

#To run labelimg
cd labelimg
python3 labelimg.py

#How to Use?
1. Choose yolo format
2. Choose save directory    # Where the annotation.txt file will go
3. Choose working directory # Where the images/dataset is
```

Polygon Segmentation - Use label-studios ([Github repo](https://github.com/heartexlabs/label-studio))
```bash
# Requires 3.7>= Python version <=3.9

#To install label-studio
pip3 install label-studio

#To run label-studio
label-studio

#How to Use?
1. Go to settings > labeling interface > Browse templates
2. Choose Semantic Segmentation with Polygons
3. Annotate
4. Export to coco format
5. Input coco format files into roboflow #https://roboflow.com
6. Export to yolov5/yolov7 pytorch format
```

**While Annotating** - Check for dirty dataset such as:
- Blurred image
- Over/Under-exposed image
- Unable to identify features of object to detect

---
### _**Things to do before continuing**_
- Install jupyter notebook
    1. Locally
        - pip install notebook
    2. Anaconda
        - [Step by step guide](https://docs.anaconda.com/anaconda/install/windows/)
- Choose Yolo Framework
    - [YoloV5](https://github.com/Evzen-T/easy2yolo#go-to-yv5-on-terminal)
    - [YoloV7](https://github.com/Evzen-T/easy2yolo#go-to-yv7-on-terminal)
---
# Go to yv5 on terminal
## **Virtual Environment**
1. python3 -m venv virtualv5
2. source virtualv5/bin/activate **OR** source virtualv5/scripts/activate
3. pip install opencv-python
4. pip install blobconverter
5. pip install depthai
6. pip install depthai-sdk

## **4 - YoloV5 Training**
1. Run jupyter notebook
    - Locally
        ```
        jupyter notebook
        ```
        find to easy2yolo/yv5/training.ipynb

    - Anaconda
        1. Search for anaconda navigator on terminal/search bar
        2. Open jupyter notebook
        3. Click on Upload
        4. Search for easy2yolo/yv5/training.ipynb
2. Edit yaml file in yolov5 folder ([template](./data.yaml))
3. Run dependencies commands
4. Choose yolov5 pretrain weights
5. Run training command
6. Locate trained pt weights (./yolov5/runs/train/exp)

## **5 - YoloV5 Conversion**
1. Setup conversion file
cd easy2yolo/yv5
Edit fpath to location of trained yolov5 pt weights on conversion.py

2. Run conversion
python3 conversion.py

## **6 - YoloV5 Inference**
- Inference with **Webcam/camera in general**
    - **Pytorch**
        1. Go to inference/pt_cam.py
        2. Change pt weights file path
        3. Run 'python3 pt_cam.py'

- Inference with **Oak camera**
    - **Pytorch**
        1. Go to inference/pt_oak.py
        2. Change pt weights file path
        3. Run 'python3 pt_oak.py'
    - **Blob**
        1. Go to inference/blob_oak.py
        2. Change blob weights file path
        3. Run 'python3 blob_oak.py'

- Inference with **Images**
    - **Pytorch**
        1. Go to inference/pt_images.py
        2. Change pt weights file path
        3. Change test image file path
        4. Run 'python3 pt_images.py'

---
# Go to yv7 on terminal
## **Virtual Environment**
1. python3 -m venv virtualv7
2. source virtualv7/bin/activate **OR** source virtualv7/scripts/activate

## **4 - YoloV7 Training**
1. Run jupyter notebook
    - Locally
        ```
        jupyter notebook
        ```
        find to easy2yolo/yv7/training.ipynb

    - Anaconda
        1. Search for anaconda navigator on terminal/search bar
        2. Open jupyter notebook
        3. Click on Upload
        4. Search for easy2yolo/yv7/training.ipynb

2. Edit yaml file in yolov5 folder ([template](./data.yaml))
3. Run dependencies commands
4. Choose yolov7 pretrain weights
5. Run training command
6. Locate trained pt weights (./yolov7/runs/train/exp)

## **5 - YoloV7 Conversion**
1. Setup conversion file
cd easy2yolo/yv7
Edit fpath to location of trained yolov7 pt weights on conversion.py

2. Run conversion
python3 conversion.py

## **6 - YoloV7 Inference**
- Inference with Webcam
    - Pytorch
        1. Go to easy2yolo/yv7/pt_cam.py
        2. Change pt weights file path
        3. Run 'python3 pt_cam.py'

- Inference with Oak camera
    - Pytorch
        1. Go to easy2yolo/yv7/pt_oak.py
        2. Change pt weights file path
        3. Run 'python3 pt_oak.py'
    - Blob
        1. Go to easy2yolo/yv7/blob_oak.py
        2. Change blob weights file path
        3. Run 'python3 blob_oak.py'

- Inference with Images
    - Pytorch
        1. Go to easy2yolo/yv7/pt_images.py
        2. Change pt weights file path
        3. Run 'python3 pt_images.py'