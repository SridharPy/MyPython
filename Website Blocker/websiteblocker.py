#Variables required:
#one for path of hostfile
#one for the list of website to be blocked
#one for loopback ip 127.0.0.1
from datetime import datetime as dt
import time

host_path_t = r"C:\Z Virtual Machines\Python Code\Website Blocker\hosts"
host_path = r"C:\Windows\System32\drivers\etc\hosts"
block_website = ["www.facebook.com","facebook.com","www.xnxx.com","www.xvideos.com","www.youporn.com","www.pornhum.com","www.login.live.com","account.live.com"]
# this cna be included in above list when needed "www.amazon.in","www.amazon.com","www.flipkart.com","www.snapdeal.com","www.ebay.in","www.ebay.com"
loop_back = "127.0.0.1"
#print(dt.now()) print like 2017-10-26 11:49:16.906423
#print(dt(dt.now().year, dt.now().month, dt.now().day, 8)) #prints like 2017-10-26 08:00:00

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 18):
        print("Work Hours!!")
        with open(host_path,"r+") as host_file:
            content = host_file.read()
            for website in block_website:
                if website in content:
                    pass
                else:
                    host_file.write(loop_back + " " + website + "\n")
    else:
        print("Enjoy! no internet restrictions, Fun Hours!!")
        with open(host_path,"r+") as host_file:
            content = host_file.readlines()
            host_file.seek(0) #moving the cursor at the begining after readline() as it moves cursor to the end of file
            for line in content:
                if not any(website in line for website in block_website): #loops each item in block_website list and comares agains the specific line in content which is holding each line of the hos_file as list
                    host_file.write(line) #if those block webside line is found that is  ot written
            host_file.truncate() #As the each new line is written above the existing lines in file once for loop finishes all the following or old content is dleeted
            #if host_file.seek(0) wasn't used the truncate will delete nothing as the new lines weree ritten at the nod exisiting lines and after tye new lines are wroitten nothing would eb taher to runcate
            #So for loop above will keep appening the lines again and again in the host_file
    time.sleep(5)
