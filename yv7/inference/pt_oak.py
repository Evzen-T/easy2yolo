import torch
import numpy as np
import cv2
import depthai as dai

model = torch.hub.load('../yolov7', 'custom', path='../yolov7/runs/train/exp/weights/best.pt', source='local', force_reload=True)

# Create pipeline
pipeline = dai.Pipeline()

# Define sources and outputs
ccenter = pipeline.create(dai.node.ColorCamera)
xout_ccenter = pipeline.create(dai.node.XLinkOut)
xout_ccenter.setStreamName('center')

# Properties
ccenter.setBoardSocket(dai.CameraBoardSocket.RGB)
ccenter.setResolution(dai.ColorCameraProperties.SensorResolution.THE_1080_P)
ccenter.setColorOrder(dai.ColorCameraProperties.ColorOrder.RGB)

# Linking
ccenter.video.link(xout_ccenter.input)

#To rescale the frame of the video capture
def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

with dai.Device(pipeline) as device:
    qcenter = device.getOutputQueue(name="center", maxSize=4, blocking=False)
    print('Webcam Online ...')
    while True:
        #Color cam feed
        inCenter = qcenter.get().getCvFrame()
        
        # Make decisions
        results = model(inCenter)
        squeezed = np.squeeze(results.render())

        # Rescale the frame of the GUI
        rescaled = rescale_frame(squeezed, percent=50)

        # Render to the screen
        cv2.imshow('Yolov7',rescaled)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

inCenter.release()
cv2.destroyAllWindows()