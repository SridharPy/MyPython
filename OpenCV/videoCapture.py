import cv2,time

video = cv2.VideoCapture(0) #triggers video object
# index 0 for first cam, 1 if second cam and so on
#Or we can provide the video file path insead of index like movie.mp4
no_of_frames = 1
while True:
    no_of_frames = no_of_frames +1
    check, frame = video.read() # first variable  validates if frame is captured,
    #second variable stores the first image form the camera and saves in the frame varable, its a numpy multi dimeantional array in BGR
    print(check)
    print(frame)

    gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #Converts BGR into grayscale

    cv2.imshow("TestFrame",gray_img)

    #time.sleep(3) #Waits for 3 seconds
    key = cv2.waitKey(1) #each fram waits for 1 milli second before next
    if key==ord('q'):
        break
print(no_of_frames)
video.release() #here we relase the camera
cv2.destroyAllWindows
