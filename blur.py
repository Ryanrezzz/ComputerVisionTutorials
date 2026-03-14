import cv2 

img_path= "/Users/ryanmaroof/ml and dl projects/ComputerVision/Photos:videos/freelancer.png"


image = cv2.imread(img_path)

k=11
norm_blur=cv2.blur(image,(k,k))
guass_blur = cv2.GaussianBlur(image,(k,k),6)
median_blur = cv2.medianBlur(image,k)


cv2.imshow('image',image)
cv2.imshow('norm_blur',norm_blur)
cv2.imshow('guass_blur',guass_blur)
cv2.imshow('median_blur',median_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
