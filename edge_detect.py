import cv2
import numpy as np
img_path= "/Users/ryanmaroof/ml and dl projects/ComputerVision/Photos:videos/player.png"

image = cv2.imread(img_path)

edge_img= cv2.Canny(image, 100, 200)

dil_img=cv2.dilate(edge_img,np.ones((3,3),dtype=np.int8))
erod_img=cv2.erode(edge_img,np.ones((1,1),dtype=np.int8))

cv2.imshow('edge_img',edge_img)
cv2.imshow('image',image)
cv2.imshow('dil_img',dil_img)
cv2.imshow('erod_img',erod_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

