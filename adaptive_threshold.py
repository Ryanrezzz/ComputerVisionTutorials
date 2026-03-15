import cv2

image_path = '/Users/ryanmaroof/ml and dl projects/ComputerVision/Photos:videos/handwritting.png'

image = cv2.imread(image_path)

gray_img=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

ret,thresh_img = cv2.threshold(gray_img,127,255,cv2.THRESH_BINARY)
adaptive_thresh= cv2.adaptiveThreshold(gray_img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,17,2)

cv2.imshow('image',image)
cv2.imshow('gray_img',gray_img)
cv2.imshow('thresh_img',thresh_img)
cv2.imshow('adaptive_thresh',adaptive_thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()