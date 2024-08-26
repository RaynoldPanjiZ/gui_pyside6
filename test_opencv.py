import cv2


# url = "vid/test1.mp4"
url = "rtsp://admin:aery2021!@192.168.45.166:554/cam/realmonitor?channel=1&subtype=0&unaicast=true&proto=Onvif"
cap = cv2.VideoCapture(url)

while True:
    ret, frame = cap.read()
    print(frame.shape)

    cv2.imshow("frame", frame)
    key = cv2.waitKey(50)
    if key == 27:
        break
cv2.destroyAllWindows()
