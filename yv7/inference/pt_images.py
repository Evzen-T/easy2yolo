import torch
import numpy as np
import cv2

model = torch.hub.load('../yolov7', path='../yolov7/runs/train/exp/weights/best.pt', source='local', force_reload=True)

img = './path2img/name.jpg'

while True:

    results = model(img)
    squeezed = np.squeeze(results.render())

    # Render to the screen
    cv2.imshow('Yolov7',squeezed)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()