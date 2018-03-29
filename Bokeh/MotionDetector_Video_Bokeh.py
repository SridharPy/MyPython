#Here first_frame will be taken as refrence for static background
#Any changes wrt that will be considered a change
import cv2, time
from datetime import datetime
import pandas

first_frame = None #Varable to grab first frame from the camera
video= cv2.VideoCapture(0) #Caputre from first webcam in laptop
status_list=[None,None]  #Using variable to store status, initial is None,None for the if condition below
times=[] #To store entry and exit time of object
df = pandas.DataFrame(columns=["Start","End"]) #Creating a pandas dataframe to store start and end times image.

while True:

    check, frame = video.read()
    status = 0 #Set status =0 for initial no change and subsequent no change
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
        if cv2.contourArea(contour) < 10000:
            continue
        status = 1 #If any moving objcet greater than 10000 pixel is detected then status changes to 1
        (x,y,w,h) = cv2.boundingRect(contour) #provides cootinates and width and height of contour < 1000
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1) #draw rectanle on the contour < 1000
        #passing color frame, x,y cordinates, then coordinates for rect right bottom corner
        #Color of rect and the last param is the with of rectangle line

    status_list.append(status) #Storing status changes in status_list, it stores 0s and 1s based on object entry and exit.
    status_list=status_list[-2:] #Code Improvement to remove unnecessary data from status list as we are interested in only last two values
    #Saves memory, makes code memeory efficient
    if status_list[-1]==1 and status_list[-2]==0: #Record time for entry of objetc
        times.append(datetime.now())
    if status_list[-1]==0 and status_list[-2]==1: #Record time for exit of object
        times.append(datetime.now())

    cv2.imshow("Gray Blurred",gray_frame) #shows blurred gray frame
    cv2.imshow("Delta Frames",gray_frame_delta) #shows delta frame
    cv2.imshow("Threhold",gray_frame_thresh)#Shows delta pixels above 30 in white
    cv2.imshow("Color Frames",frame)

    key = cv2.waitKey(1)
    #print(gray_frame) #Prim=nts numpy array of each frame
    if key==ord('q'):
        if status == 1: #this will record time when q was pressed while moving object was in the frame
            times.append(datetime.now()) #Add current time to times if object is there at exit
        break

    #print(status) #Prints the status 0 or 1 based on wether moving object is found or not
print(status_list)
print(times)

for i in range(0,len(times),2): #loops through length of times list with + 2 skip for next loop
    df=df.append({"Start":times[i],"End":times[i+1]}, ignore_index=True) #Insert start and end time in to pandas data frame


df.to_csv("time_tracker.csv") #Write value of pandas data frame into a csv file.
video.release()
cv2.destroyAllWindows()
