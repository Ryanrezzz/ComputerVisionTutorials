import cv2

image_path="/Users/ryanmaroof/ml and dl projects/ComputerVision/Photos:videos/cake.png"

image= cv2.imread(image_path)
print(image.shape)


resized_img= cv2.resize(image,(200,306))
print(resized_img.shape)

cv2.imshow('image',image)
cv2.imshow('resized_img',resized_img)

cv2.waitKey(0)
cv2.destroyAllWindows()