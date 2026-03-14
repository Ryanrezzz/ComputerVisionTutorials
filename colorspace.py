import cv2

image_path= "/Users/ryanmaroof/ml and dl projects/ComputerVision/Photos:videos/bird.png"

img=cv2.imread(image_path)


rgb_img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
gray_img= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
hsv_img= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.imshow('bgr img',img)
cv2.imshow('rgb img',rgb_img)
cv2.imshow('gray img',gray_img)
cv2.imshow('hsv img',hsv_img)
cv2.waitKey(0)
cv2.destroyAllWindows()