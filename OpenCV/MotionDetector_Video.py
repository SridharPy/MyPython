#Here first_frame will be taken as refrence for static background
#Any changes wrt that will be considered a change
import cv2, time

first_frame = None #Varable to grab first frame from the camera
video= cv2.VideoCapture(0) #Caputre from first webcam in laptop

while True:

    check, frame = video.read()

    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#conert each frame to grayscale
    #Applying gaussian blur to rmove noise and for more accurate comparison of images
    gray_frame = cv2.GaussianBlur(gray_frame,(21,21),0)
    #Takes first parameter as the image,
    #second tuple parameter is for width and heght of Gaussian kernel, 21 is accepted number, parameters for blurriness
    #third parameter os the standard deviation
    #docs.opencv.org for more information on gaussian parameters

    if first_frame is None:
        first_frame = gray_frame #First frame will be grabbed here
        continue

    #Here we take delta between first frame and current frame (both blurred)
    gray_frame_delta = cv2.absdiff(first_frame, gray_frame)

    #Here we set a threhoold limit and set white (255) for all those delta pixels whose value are above 30 in numpy array
    gray_frame_thresh = cv2.threshold(gray_frame_delta,30,255,cv2.THRESH_BINARY)[1]
    #Threhold method returns a tuple, first item of the tuple is  value of the threshold limit (which is 30 here)
    #For the THRESHOLD_BINARY method used here we need to access only the second item of the tuple which is the actual frame
    #So we specify [1] to access second item
    #docs.opencv.org cv2.threshold for more info

    #Here we dilate the threshold image by smoothening it
    #For advanced processing we can pass the kenel arrayin second parameter
    #Third parameter if for iteration more it is more smooth the iagne would be
    gray_frame_thresh = cv2.dilate(gray_frame_thresh,None,iterations = 2)

    #Now we find contours on the threhold delta images
    #for opnecv2 with python 2 we cna use (cnts,_)
    #first parameter is image, we used copy of the threshold image by usning copy method
    #Second parameter is the method whch finds or retrieves contour from image
    #thrid param is the appoximaton method that opencv will apply for retiving the contour
    #We will no get all contours for distinct images. All these contours will be saved in cnts variable which is a list
    (_,cnts,_) = cv2.findContours(gray_frame_thresh.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    #We draw a rectangle around the contour if the pixel count of objects's contour are < 1000

    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue
        (x,y,w,h) = cv2.boundingRect(contour) #provides cootinates and width and height of contour < 1000
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1) #draw rectanle on the contour < 1000
        #passing color frame, x,y cordinates, then coordinates for rect right bottom corner
        #Color of rect and the last param is the with of rectangle line


    cv2.imshow("Gray Blurred",gray_frame) #shows blurred gray frame
    cv2.imshow("Delta Frames",gray_frame_delta) #shows delta frame
    cv2.imshow("Threhold",gray_frame_thresh)#Shows delta pixels above 30 in white
    cv2.imshow("Color Frames",frame)

    key = cv2.waitKey(1)
    print(gray_frame) #Prim=nts numpy array of each frame

    if key==ord('q'):
        break

video.release()
cv2.destroyAllWindows()
