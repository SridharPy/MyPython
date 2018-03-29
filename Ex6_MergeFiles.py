"""Here we are reading the content from of three files from same directory
and appending the content of each file into a single file with name as the current timestamp at microsecond level
 """
import datetime
import glob2

file_lst= (glob2.glob('file*.txt')) #lists the files with name starting as file and of txt format and stores all the names in file_lst list
with open(datetime.datetime.now().strftime("%Y-%m-%d__%H-%M-%S-%f")+".txt",'a+') as file: #Creates and opens a file with a name of current date timestamp at microsecond level
        for lst in file_lst: #iterates through each file
            with open(lst,'r') as file1:
                file.write(file1.read()+"\n") # Reading the content of current file in the lsit and appending it to tyhe new file having the name as timestamp
