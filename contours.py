import cv2


img_path = "/Users/ryanmaroof/ml and dl projects/ComputerVision/Photos:videos/birdsWhite.png"

img = cv2.imread(img_path)

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh_img = cv2.threshold(gray_img,127,255,cv2.THRESH_BINARY_INV)

countours,hierarchy = cv2.findContours(thresh_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for cont in countours:
     if  cv2.contourArea(cont)>1000:
         cv2.drawContours(img,cont,-1,(0,255,0),2)
         x1,y1,w1,h1 = cv2.boundingRect(cont)
         cv2.rectangle(img,(x1,y1),(x1+w1,y1+h1),(0,255,0),2)

cv2.imshow('img',img)
cv2.imshow('gray_img',gray_img)
cv2.imshow('thresh_img',thresh_img)
cv2.waitKey(0)
cv2.destroyAllWindows()