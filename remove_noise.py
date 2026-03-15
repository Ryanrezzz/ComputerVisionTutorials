import cv2

image_path = "/Users/ryanmaroof/ml and dl projects/ComputerVision/Photos:videos/noisy_image.png"

image = cv2.imread(image_path)


median_correcct_img= cv2.medianBlur(image,7)

cv2.imshow('image',image)
cv2.imshow('median_correcct_img',median_correcct_img)
cv2.waitKey(0)
cv2.destroyAllWindows()