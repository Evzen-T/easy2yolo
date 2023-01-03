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
    
    eg. problem : Security issue, Safety issue

- What object are you detecting?

    eg. solution : Face (Facial Recognition), Helmet (Object Detection)

## **2 - Dataset Collection**
- What method are you using to collect data?
    1. Camera/Webcam - Use dataset_collection/**cam.py**
    2. Oak camera - Use dataset_collection/**oak.py**
    3. Online sources - Use Open Images Dataset ([OIDv7](https://storage.googleapis.com/openimages/web/visualizer/index.html)) by google

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
### **Things to do before continuing**
- Install **jupyter notebook**
    1. Locally
        - pip install notebook
    2. Anaconda
        - [Step by step guide](https://docs.anaconda.com/anaconda/install/windows/)
- Choose **Yolo Framework**
    - YoloV5 [Training](yv5/training.ipynb) / [Github repo](https://github.com/ultralytics/yolov5)
    - YoloV7 [Training](yv7/training.ipynb) / [Github repo](https://github.com/WongKinYiu/yolov7)

- **Virtual Environment**

    - YoloV5
        1. python3 -m venv virtualv5
        2. source virtualv5/bin/activate **OR** source virtualv5/scripts/activate

    - YoloV7
        1. python3 -m venv virtualv7
        2. source virtualv7/bin/activate **OR** source virtualv7/scripts/activate


    3. pip install opencv-python
    4. pip install blobconverter
    5. pip install depthai
    6. pip install depthai-sdk
    7. pip install onnx
    8. pip install onnxruntime
    9. pip install onnxsim

### **To Note**
- YoloV5 & YoloV7 are different repositories, thus different way of loading models.
- Use respective inference python files

## **4 - Training**
1. Run jupyter notebook
    - Locally
        ```
        jupyter notebook
        ```
        find to ./yv5/training.ipynb **OR** ./yv7/training.ipynb

    - Anaconda
        1. Search for anaconda navigator on terminal/search bar
        2. Open jupyter notebook
        3. Click on Upload
        4. Search for easy2yolo/yv5/training.ipynb **OR** easy2yolo/yv7/training.ipynb



2. Edit yaml file in yolov5 **or** yolov7 folder ([template](./data.yaml))
3. Run dependencies commands
4. Choose yolov5 **or** yolov7 pretrain weights
5. Run training command
6. Locate trained pt weights (./yolov5/runs/train/exp/weights **or** ./yolov7/runs/train/exp/weights)

## **5 - Conversion**
1. Setup conversion file
- cd easy2yolo/yv5 **OR** cd easy2yolo/yv7
- Edit fpath to location of trained pt weights on conversion.py

2. Run conversion
python3 conversion.py

## **6 - Inference**

Inference with **Webcam/camera**
- **Pytorch**
    1. Go to inference/pt_cam.py
    2. Change pt weights file path
    3. Run 'python3 pt_cam.py'

Inference with **Oak camera**
- **Pytorch**
    1. Go to inference/pt_oak.py
    2. Change pt weights file path
    3. Run 'python3 pt_oak.py'
- **Blob**
    1. Go to inference/blob_oak.py
    2. Change blob weights file path
    3. Run 'python3 blob_oak.py'

Inference with **Images**
- **Pytorch**
    1. Go to inference/pt_images.py
    2. Change pt weights file path
    3. Change test image file path
    4. Run 'python3 pt_images.py'