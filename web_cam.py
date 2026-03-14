import cv2

web_cam= cv2.VideoCapture(0)


while True:
    ret,frame = web_cam.read()

    cv2.imshow('frame',frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

web_cam.release()
cv2.destroyAllWindows()