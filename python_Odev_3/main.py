import cv2
import numpy as np


image=cv2.imread("princ.png.jpg") #görüntüyü okuyor
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) #görüntüyü grileştriyor

ret,thresh1=cv2.threshold(gray,70,255,cv2.THRESH_BINARY)  #eşikleme uygulanıyor

kernel=np.ones((5,5),np.uint8)# çekirdeğini buluyor


#erions ile dilation ile morfolojik işlem uygulanıyor
erions=cv2.erode(thresh1,kernel,iterations=1)
dilations=cv2.dilate(erions,kernel,iterations=1)

#konturleme yapılıyor ve görüntü BGR dan RGB ye dönüştürülüyor
(cnt, hierarchy) = cv2.findContours(
    dilations.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.drawContours(rgb, cnt, -1, (0, 255, 0), 2)


cv2.imshow("original",image)
cv2.imshow("rgb",rgb)

print("Princ sayısı : ", len(cnt))

cv2.waitKey(0)
cv2.destroyAllWindows()

