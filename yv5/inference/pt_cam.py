import torch
import numpy as np
import cv2

model = torch.hub.load('ultralytics/yolov5', 'custom', path='../yolov5/runs/train/exp/weights/best.pt', force_reload=True)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS,30)

while cap.isOpen():
    ret, frame = cap.read()
    if not ret:
        continue

    results = model(frame)
    squeezed = np.squeeze(results.render())

    # Render to the screen
    cv2.imshow('Yolov5',squeezed)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()