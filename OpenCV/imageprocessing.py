import cv2

face_cascade = cv2.CascadeClassifier("C:\Sridhar\Z1\Learnings\Python\Codes\Programs\OpenCV\Files\haarcascade_frontalface_default.xml")
#This is an xml cascade file for frontal face needs to be downloaded for the web for different cascades like side face etc.
#img = cv2.imread("C:\Sridhar\Z1\Learnings\Python\Codes\Programs\OpenCV\Files\photo.jpg") # Sngle face
img = cv2.imread("C:\Sridhar\Z1\Learnings\Python\Codes\Programs\OpenCV\Files\multi_face.jpg") #multi face
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #Converts color to gray scale, it is helpful for face detection

#Creating face co-ordinates with in the image to identifie face in the Image
#using the face_cascade which is storing frontal face cascade exemplary
#Using detectMultiScale method
#scaleFactor 1.05 downscales image to 5% each time till the face cordinates are detected
#We can test and set it for accuracy
#minNeighbor tells how many neighbor to check around the window and test and set for accuracy
face = face_cascade.detectMultiScale(gray_img,
scaleFactor=1.12,
minNeighbors=5)

print(face)#it s a numpy.ndarray numpy n dimensional array
print(type(face))#Prints the face variable value the below value is for single face.
#For multi face the we will have list for each face
#[[155  83 382 382]] where first value says 155th column in the Image
#second value is 83rd row fromimange
#third value is width which is 382
#Fourth column is the height 382

#Draw a rectangle on the detected face in the Image

for x,y,w,h in face:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(100,200,255),1)
    #draws rectangle on image, first tuple takes upper left x,y cortinates
    #and next tuple takes lower right coordinates.
    #theird argument take BGR value which can be between 0-255 for each
    #fourth argument s thickness of recantgle line

img_resize = cv2.resize(img,(int(img.shape[1]/1),int(img.shape[0]/1)))
cv2.imshow("Image",img_resize)
cv2.waitKey(0)
cv2.destroyAllWindows
