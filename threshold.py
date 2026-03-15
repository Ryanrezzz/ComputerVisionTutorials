import cv2

image_path = '/Users/ryanmaroof/ml and dl projects/ComputerVision/Photos:videos/bear.png'

image = cv2.imread(image_path)

gray_img=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

ret,thresh_img = cv2.threshold(gray_img,127,255,cv2.THRESH_BINARY)

cv2.imshow('image',image)
cv2.imshow('gray_img',gray_img)
cv2.imshow('thresh_img',thresh_img)
cv2.waitKey(0)
cv2.destroyAllWindows()