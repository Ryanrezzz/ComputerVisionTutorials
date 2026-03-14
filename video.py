import cv2
video_path = "/Users/ryanmaroof/ml and dl projects/ComputerVision/Photos:videos/pinkpantheress.mp4"

video = cv2.VideoCapture(video_path)

ret=True

while ret:
    ret,frame=video.read()
   
    if ret:
         cv2.imshow('frame',frame)
         cv2.waitKey(30)

video.release()
cv2.destroyAllWindows()
