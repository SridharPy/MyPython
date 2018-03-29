import paramiko
import pandas
import openpyxl
import xlsxwriter


read_Afdwe = ""
read_Afdwd=""
server='web1.local'
user= 'root'
pwd= 'Shiva@123'
file_Afdwe= "APAC-FolderDocument-Weekend-Job-Errors.csv"
command_Afdwe= 'cat /root/Downloads/APAC-weekend-analyze-folderdocument-tables.out| egrep -i -B1 "memory|error|exception|critical"'
file_Ailwe= "APAC-idlookup-weekend-analyze-Errors.csv"
command_Ailwe = 'cat /root/Downloads/APAC-weekend-analyze-idlookup-tables.out| egrep -i -B1 "memory|error|exception|critical"'
file_Arwe= "APAC-route-weekend-analyze-Errors.csv"
command_Arwe = 'cat /root/Downloads/APAC-weekend-analyze-route-tables.out| egrep -i -B1 "memory|error|exception|critical"'
file_Acttd= "APAC-Clear-Temp-Tables-Daliy-Errors.csv"
command_Acttd = 'cat /root/Downloads/APAC-Daily_ClearTempTables.out| egrep -i -B1 "memory|error|exception|critical"'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #adds host key for known host
client.connect(server,username=user,password=pwd)

stdin_Afdwe, stdout_Afdwe, stderr_Afdwe = client.exec_command(command_Afdwe)
stdin_Ailwe, stdout_Ailwe, stderr_Ailwe = client.exec_command(command_Ailwe)
stdin_Arwe, stdout_Arwe, stderr_Arwe = client.exec_command(command_Arwe)
stdin_Acttd, stdout_Acttd, stderr_Acttd = client.exec_command(command_Acttd)

stdout_Afdwe = stdout_Afdwe.readlines()
stdout_Ailwe = stdout_Ailwe.readlines()
stdout_Arwe = stdout_Arwe.readlines()
stdout_Acttd = stdout_Acttd.readlines()

client.close()

with open(file_Afdwe,'w+') as file:
    for i in stdout_Afdwe:
        file.write(str(i.replace("\n"," ===>> ")))

        if "--" in i:
            file.write(i.replace("--","\n"))
    file.seek(0)
    read_Afdwe=file.read()



with open(file_Ailwe,'w+') as file:
    for i in stdout_Ailwe:
        file.write(str(i.replace("\n"," ===>> ")))
        if "--" in i:
            file.write(i.replace("--","\n"))
    file.seek(0)
    read_Ailwe=file.read()

with open(file_Arwe,'w+') as file:
    for i in stdout_Arwe:
        file.write(str(i.replace("\n"," ===>> ")))
        if "--" in i:
            file.write(i.replace("--","\n"))
    file.seek(0)
    read_Arwe=file.read()


with open(file_Acttd,'w+') as file:
    for i in stdout_Acttd:
        file.write(str(i.replace("\n"," ===>> ")))
        if "psql" in i:
            file.write(i.replace("psql","\n"))
    file.seek(0)
    read_Acttd=file.read()


if read_Afdwe != "":
    df1=pandas.read_table(file_Afdwe,header=None,names=["Skipped Partitons"])

else:
    df1=pandas.DataFrame(["No Errors Found in FolderDocument Weekend Analyze job"])



if read_Ailwe != "":
    df2=pandas.read_table(file_Ailwe,header=None,names=["Skipped Partitons"])


else:
    df2=pandas.DataFrame(["No Errors Found in IDLookup Weekend Analyze Job"])


if read_Arwe != "":
    df3=pandas.read_table(file_Arwe,header=None,names=["Skipped Partitons"])


else:
    df3=pandas.DataFrame(["No Errors Found in Route Weekend Analyze Job"])

if read_Acttd != "":
    df4=pandas.read_table(file_Acttd,header=None,names=["Skipped Partitons"])


else:
    df4=pandas.DataFrame(["No Errors Found in Clear Temp Table Daily Job"])


writer = pandas.ExcelWriter('APAC.xlsx', engine='xlsxwriter')
df1.to_excel(writer, sheet_name='FoderDoc_WeekEnd')
df2.to_excel(writer,sheet_name="IDLookup_WeekEnd")
df3.to_excel(writer,sheet_name="Route_WeekEnd")
df4.to_excel(writer,sheet_name="Clear_Temp_Table_Daily")
writer.close()
