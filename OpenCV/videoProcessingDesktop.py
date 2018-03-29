"""This prgram captures images from laptop camera and tracks the face"""
import cv2,time

face_cascade = cv2.CascadeClassifier("D:\Python\Codes\OpenCV\Files\haarcascade_frontalface_default.xml")

video = cv2.VideoCapture("D:\Python\Codes\OpenCV\Files\\test_video.mp4") #triggers video object
# index 0 for first cam, 1 if second cam, 3 for next cam and so on
#Or we can provide the video file path insead of camera index e.g. movie.mp4
no_of_frames = 1
while True:
    no_of_frames = no_of_frames +1
    check, frame = video.read()
    # first variable  validates if frame is captured,
    #second variable stores the first image form the camera and saves in the frame varable, its a numpy multi dimeantional array in BGR
    print(check) #Prints  if video is caputre or cam is available
    print(frame) # Prints numpy array for each frame or image

    gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #Converts BGR into grayscale

    face = face_cascade.detectMultiScale(gray_img,
    scaleFactor=1.12,
    minNeighbors=5)
    #downscales grayed image to 5% and checks 5 neighbours around window

    for x,y,w,h in face:
       frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,200,255),1)

    cv2.imshow("TestFrame",frame)

    #time.sleep(3) #Waits for 3 seconds
    key = cv2.waitKey(1) #each fram waits for 1 milli second before next
    if key==ord('q'):
        break
print("Frames : ", no_of_frames)
video.release() #here we relase the camera
cv2.destroyAllWindows
