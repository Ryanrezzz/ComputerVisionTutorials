import cv2

img_path = '/Users/ryanmaroof/ml and dl projects/ComputerVision/Photos:videos/board.png'

img = cv2.imread(img_path)
print(img.shape)

cv2.line(img,(300,300),(300,1000),(0,255,0),3)

cv2.rectangle(img,(320,320),(800,800),(0,0,255),5)

cv2.circle(img,(1000,1000),100,(255,0,0),5)

cv2.putText(img,"How are you?",(900,800),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),2)

cv2.imshow('img',img)

cv2.waitKey(0) 
cv2.destroyAllWindows()