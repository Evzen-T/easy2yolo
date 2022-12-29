import torch
import numpy as np
import cv2

model = torch.hub.load('../yolov7', 'custom', path='../yolov7/runs/train/exp/weights/best.pt', source='local', force_reload=True)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS,30)

while cap.isOpen():
    ret, frame = cap.read()
    if not ret:
        continue

    results = model(frame)
    squeezed = np.squeeze(results.render())

    # Render to the screen
    cv2.imshow('Yolov7',squeezed)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()