# **Easy to Yolo**
## **A Easy step by step guide to YoloV5 & YoloV7**
1. [Decide on object to detect](https://github.com/Evzen-T/easy2yolo#1---decide-on-object-to-detect)
2. [Dataset Collection](https://github.com/Evzen-T/easy2yolo#2---dataset-collection)
3. [Dataset Annotation + Cleaning](https://github.com/Evzen-T/easy2yolo#3---dataset-annotation--cleaning)
4. [Training](https://github.com/Evzen-T/easy2yolo#4---training)
5. [Conversion](https://github.com/Evzen-T/easy2yolo#5---conversion)
6. [Inference](https://github.com/Evzen-T/easy2yolo#6---inference)

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
        1. cd yv5

        2. python3 -m venv virtualv5

        3. source virtualv5/bin/activate **OR** source virtualv5/scripts/activate

        4. pip install -r requirements.txt

    - YoloV7
        1. cd yv7

        2. python3 -m venv virtualv7

        3. source virtualv7/bin/activate **OR** source virtualv7/scripts/activate

        4. pip install -r requirements.txt

- **To Note for part 4 - 6**

    - YoloV5 & YoloV7 have different ways of loading models.

    - Use respective python files

## **4 - Training**
1. Run jupyter notebook
    - Locally
        ```
        jupyter notebook
        ```
        find to ./training.ipynb

    - Anaconda
        - Search for anaconda navigator on terminal/search bar
        - Open jupyter notebook
        
        - Click on Upload
        - Search for ./training.ipynb

2. Edit yaml file in **yolov5**/**yolov7** folder ([template](./data.yaml))
3. Run dependencies commands
4. Choose **yolov5**/**yolov7** pretrain weights
5. Run training command
6. Locate trained pt weights (./yolov5/runs/train/exp/weights **or** ./yolov7/runs/train/exp/weights)

## **5 - Conversion**
1. Setup conversion file

- cd /yv5 **OR** cd /yv7

- Edit fpath to location of trained pt weights on conversion.py

2. Run conversion
- python3 conversion.py

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