import cv2

img_path="/Users/ryanmaroof/ml and dl projects/ComputerVision/Photos:videos/cake.png"

#read
image= cv2.imread(img_path)

#write
cv2.imwrite("new_image.jpg", image)

#display
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()