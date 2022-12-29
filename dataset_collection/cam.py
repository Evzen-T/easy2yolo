import cv2

img_counter = 0
folder_name = './images_taken'

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS,30)

#To rescale the frame of the video capture
def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue
    # rescaled = rescale_frame(frame, percent=50)
    cv2.imshow("Cam", frame)
    
    k = cv2.waitKey(1)
    if k%256 == 27:
        print("Escape hit, closing app")
        break
    elif k%256 == 32:
        img_name = folder_name + "/Frame_{}.jpg".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter+=1

cap.release()
cv2.destroyAllWindows()