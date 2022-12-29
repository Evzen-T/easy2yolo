import cv2
import depthai as dai

img_counter = 0
folder_name = './images_taken'

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
        rescaled = rescale_frame(inCenter,percent=50)
        cv2.imshow("Oak", rescaled)

        k = cv2.waitKey(1)
        if k%256 == 27:
            print("Escape hit, closing app")
            break
        elif k%256 == 32:
            img_name = folder_name + "/Frame_{}.jpg".format(img_counter)
            cv2.imwrite(img_name, inCenter)
            print("{} written!".format(img_name))
            img_counter+=1

inCenter.release()
cv2.destroyAllWindows()