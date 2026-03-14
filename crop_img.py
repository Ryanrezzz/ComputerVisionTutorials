import cv2

image_path= "/Users/ryanmaroof/ml and dl projects/ComputerVision/Photos:videos/cake.png"


image = cv2.imread(image_path)
print(image.shape)

cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cropped_image = image[100:900,200:1200]
print(cropped_image.shape)
cv2.imshow('cropped_image',cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()