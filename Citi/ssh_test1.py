import paramiko
import pandas
#import openpyxl
#import xlsxwriter


def checkMaintLogs(srv,usr,pw,file_fdwe,command_fdwe,file_ilwe,command_ilwe,file_rwe,command_rwe,file_cttd,command_cttd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #adds host key for known host
    client.connect(srv,username=usr,password=pw)

    stdin_fdwe, stdout_fdwe, stderr_fdwe = client.exec_command(command_fdwe)
    stdin_ilwe, stdout_ilwe, stderr_ilwe = client.exec_command(command_ilwe)
    stdin_rwe, stdout_rwe, stderr_rwe = client.exec_command(command_rwe)
    stdin_cttd, stdout_cttd, stderr_cttd = client.exec_command(command_cttd)

    out_fdwe = stdout_fdwe.readlines()
    out_ilwe = stdout_ilwe.readlines()
    out_rwe = stdout_rwe.readlines()
    out_cttd = stdout_cttd.readlines()

    client.close()

    with open(file_fdwe,'w+') as file:
        for i in out_fdwe:
            file.write(str(i.replace("\n"," ===>> ")))

            if "--" in i:
                file.write(i.replace("--","\n"))
        file.seek(0)
        read_fdwe=file.read()



    with open(file_ilwe,'w+') as file:
        for i in out_ilwe:
            file.write(str(i.replace("\n"," ===>> ")))
            if "--" in i:
                file.write(i.replace("--","\n"))
        file.seek(0)
        read_ilwe=file.read()

    with open(file_rwe,'w+') as file:
        for i in out_rwe:
            file.write(str(i.replace("\n"," ===>> ")))
            if "--" in i:
                file.write(i.replace("--","\n"))
        file.seek(0)
        read_rwe=file.read()


    with open(file_cttd,'w+') as file:
        for i in out_cttd:
            file.write(str(i.replace("\n"," ")))
            if "psql" in i:
                file.write(i.replace("psql","\n"))
        file.seek(0)
        read_cttd=file.read()


    if read_fdwe != "":
        df1=pandas.read_table(file_fdwe,header=None,names=["Skipped Partitons"])

    else:
        df1=pandas.DataFrame(["No Errors Found in FolderDocument Weekend Analyze job"])



    if read_ilwe != "":
        df2=pandas.read_table(file_ilwe,header=None,names=["Skipped Partitons"])


    else:
        df2=pandas.DataFrame(["No Errors Found in IDLookup Weekend Analyze Job"])


    if read_rwe != "":
        df3=pandas.read_table(file_rwe,header=None,names=["Skipped Partitons"])


    else:
        df3=pandas.DataFrame(["No Errors Found in Route Weekend Analyze Job"])

    if read_cttd != "":
        df4=pandas.read_table(file_cttd,header=None,names=["Skipped Partitons"])


    else:
        df4=pandas.DataFrame(["No Errors Found in Clear Temp Table Daily Job"])


    if "web1" in srv:
        writer = pandas.ExcelWriter('APAC.xlsx')#, engine='xlsxwriter')
        df1.to_excel(writer, sheet_name='FoderDoc_WeekEnd')
        df2.to_excel(writer,sheet_name="IDLookup_WeekEnd")
        df3.to_excel(writer,sheet_name="Route_WeekEnd")
        df4.to_excel(writer,sheet_name="Clear_Temp_Table_Daily")
        writer.close()

    elif "sec-name" in srv:
        writer = pandas.ExcelWriter('EMEA.xlsx')#, engine='xlsxwriter')
        df1.to_excel(writer, sheet_name='FoderDoc_WeekEnd')
        df2.to_excel(writer,sheet_name="IDLookup_WeekEnd")
        df3.to_excel(writer,sheet_name="Route_WeekEnd")
        df4.to_excel(writer,sheet_name="Clear_Temp_Table_Daily")
        writer.close()


#Checking Logs in Web1 providing all info for web1 server
server_web='web1.local'
user_web= 'root'
pwd_web= 'Shiva@123'
file_Afdwe= "APAC-FolderDocument-Weekend-Job-Errors.csv"
command_Afdwe= 'cat /root/Downloads/APAC-weekend-analyze-folderdocument-tables.out| egrep -i -B1 "memory|error|exception|critical"'
file_Ailwe= "APAC-idlookup-weekend-analyze-Errors.csv"
command_Ailwe = 'cat /root/Downloads/APAC-weekend-analyze-idlookup-tables.out| egrep -i -B1 "memory|error|exception|critical"'
file_Arwe= "APAC-route-weekend-analyze-Errors.csv"
command_Arwe = 'cat /root/Downloads/APAC-weekend-analyze-route-tables.out| egrep -i -B1 "memory|error|exception|critical"'
file_Acttd= "APAC-Clear-Temp-Tables-Daliy-Errors.csv"
command_Acttd = 'cat /root/Downloads/APAC-Daily_ClearTempTables.out| egrep -i -B1 "memory|error|exception|critical"'

#Checking Logs in HDP Sec, provding all info for sec-name server and log location
server_sec='sec-name.local'
user_sec= 'root'
pwd_sec= 'Shiva@123'
file_Efdwe= "EMEA-FolderDocument-Weekend-Job-Errors.csv"
command_Efdwe= 'cat /root/Downloads/EMEA-weekend-analyze-folderdocument-tables.out| egrep -i -B1 "memory|error|exception|critical"'
file_Eilwe= "EMEA-idlookup-weekend-analyze-Errors.csv"
command_Eilwe = 'cat /root/Downloads/EMEA-weekend-analyze-idlookup-tables.out| egrep -i -B1 "memory|error|exception|critical"'
file_Erwe= "EMEA-route-weekend-analyze-Errors.csv"
command_Erwe = 'cat /root/Downloads/EMEA-weekend-analyze-route-tables.out| egrep -i -B1 "memory|error|exception|critical"'
file_Ecttd= "EMEA-Clear-Temp-Tables-Daliy-Errors.csv"
command_Ecttd = 'cat /root/Downloads/EMEA-Daily_ClearTempTables.out| egrep -i -B1 "memory|error|exception|critical"'


#web1 Check logs
checkMaintLogs(server_web,user_web,pwd_web,file_Afdwe,command_Afdwe,file_Ailwe,command_Ailwe,file_Arwe,command_Arwe,file_Acttd,command_Acttd)
#HDP Sec-Name logs check
checkMaintLogs(server_sec,user_sec,pwd_sec,file_Efdwe,command_Efdwe,file_Eilwe,command_Eilwe,file_Erwe,command_Erwe,file_Ecttd,command_Ecttd)
