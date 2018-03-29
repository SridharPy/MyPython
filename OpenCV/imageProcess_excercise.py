import cv2
import glob
#import os

#img_names= os.listdir("D:\Z Virtual Machines\Python\Codes\OpenCV\")
img_names = glob.glob("*.jpg") #glob accepts *jpg which will read only  jpg files and leave others
#Code needs to be analyzed for absolute directory path D:\Z Virtual Machines\Python\Codes\OpenCV\*.jpg
#glob doesn't work but os.listdir will work if it has only image files in it

print(img_names)

for im in img_names:
    img = cv2.imread(im,0)
    img_rs= cv2.resize(img,(100,100))
    cv2.imshow("file",img_rs)
    cv2.waitKey(1000)
    cv2.destroyAllWindows
    cv2.imwrite("new_"+im,img_rs)
