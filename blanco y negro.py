import cv2   
img=cv2.imread("butterfly.jpg")
cv2.imshow("mostrar imagen",img)
gray_img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("escala de grises",gray_img)
cv2.waitkey(0)