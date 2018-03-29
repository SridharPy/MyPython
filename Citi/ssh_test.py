import paramiko
import pandas
import openpyxl
import xlsxwriter

l=[]
read_Afdwe = ""
read_Afdwd=""
server='web1.local'
user= 'root'
pwd= 'Shiva@123'
file_Afdwe= "APAC-FolderDocument-Weekend-Job-Errors.csv"
command_Afdwe= 'cat /root/Downloads/APAC-weekend-analyze-folderdocument-tables.out| egrep -i -B1 "memory|error|exception|critical"'
file_Afdwd= "APAC-FolderDocument-Daily-Job-Errors.csv"
#command_Afdwd = 'cat /root/Downloads/APAC-Daily-analyze-idlookup-currentTwoMonths-tables.out| egrep -i -B1"memory|error|exception|critical"'
command_Afdwd= 'cat /root/Downloads/APAC-weekend-analyze-folderdocument-tables.out| egrep -i -B1 "memory|error|exception|critical"'


client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #adds host key for known host
client.connect(server,username=user,password=pwd)

stdin_Afdwe, stdout_Afdwe, stderr_Afdwe = client.exec_command(command_Afdwe)
stdin_Afdwd, stdout_Afdwd, stderr_Afdwd = client.exec_command(command_Afdwd)

out_Afdwe = stdout_Afdwe.readlines()
stdout_Afdwd = stdout_Afdwd.readlines()

client.close()

with open(file_Afdwe,'w+') as file:
    for i in out_Afdwe:
        file.write(str(i.replace("\n"," ===>> ")))#+i.split("\n")[3])
        #file.write(i)
        if "--" in i:
            file.write(i.replace("--","\n"))
    file.seek(0)
    read1=file.read()
    print(read1)
    print(type(read1))
    print(len(read1))





"""
with open(file_Afdwd,'w+') as file:
    for i in stdout_Afdwd:
        file.write(i)
    file.seek(0)
    read2=file.read()
"""

if read1 != "":
    print("File1 Not Blank")
    #print(read1)
    #df1=pandas.read_table(file_Afdwe)
    df1=pandas.read_table(file_Afdwe,header=None)
    df1.to_excel("APAC1.xlsx",sheet_name="FolderDoc_WeekEnd",index_label='Sr No.', merge_cells=False)
else:
    print("file1 is blank")


"""
if read2 != "":
    #print("File2 is not blank")
    #df2=pandas.to_csv(file_Afdwd,Header=None)
    #df2=pandas.read_csv(file_Afdwe,sep=";")
    #df2.to_excel("APAC.xlsx",sheet_name="FolderDoc_WeekDay",index_label='SR No.', merge_cells=False)
    print(read2)
    #--df2=pandas.read_csv(file_Afdwd,sep="ERROR",header=None, skip_blank_lines=True,skipinitialspace=True)
    #df2.to_csv("APAC_Weekday_FolderDocument.csv")
else:
    print("file2 is blank")


#--writer = pandas.ExcelWriter('APAC.xlsx', engine='xlsxwriter')
#--df1.to_excel(writer, sheet_name='FoderDoc_WeekEnd')
#--df2.to_excel(writer,sheet_name="FolderDoc_WeekDay")
#--writer.close()

#--print(len(df1.index))
#writer = pandas.ExcelWriter('APAC.xlsx', engine='xlsxwriter')
#df2.to_excel(writer, sheet_name='FoderDoc_WeekDay')
"""
