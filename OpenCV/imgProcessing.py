import cv2

img_gray = cv2.imread("galaxy.jpg",0) #reads image in 0 for grayscale, 1 for RBG and -1 alpha RBG with transparency

img_color = cv2.imread("galaxy.jpg",1)

print(img_gray) #Prints numpy n dimensional array of image

print(img_gray.shape) #Prints Number of pixels veritcal and horizontal directions or image resolution 1485X990

print(img_gray.ndim) #Prints dimension of numpy array, here is it gray scale so 2
print(img_color.ndim)#Prints dimensions of rbg image here which is 3


cv2.imshow("Galaxy",img_gray) #Displays image Provide Any name and image path/name
cv2.waitKey(0) #Image closes on pressing any key
#cv2.waitKey(2000) #Image auto closes after 2000 milli seconds or 2 seconds
cv2.destroyAllWindows # After  2 seconds what to do - Destroy all windows

#rs_img=cv2.resize(img_color,(1000,700)) #Resizes image to said horizontal,veritcal pixels
#or resizing the original numpy array of the image, shows interpolated image on screen
#We can use shape to get original pixels and devide veritcal and horizontal by 2 or so
rs_img = cv2.resize(img_color,(int(img_color.shape[1]/2),int(img_color.shape[0]/2)))
#Here int is used as .shape /2 can provide decimal value for pixels which doesn't make sense
#Also division in python always returns float
cv2.imshow("Galaxy_Cl",rs_img)
cv2.imwrite("Galazy_RS_Write.jpg",rs_img)  # Here we are writing resized image as new image file
cv2.waitKey(0)
cv2.destroyAllWindows
