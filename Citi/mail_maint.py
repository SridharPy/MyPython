import ssh_test1
from email.mime.text import MIMEText

def  send_email():
    from_email="sridhartn83@gmail.com"
    from_password="Rani@1234"
    to_email="sridhar.gnu@gmail.com"

    subject="Testing Email Module"
    message="<strong>Maintenance Output</strong>"

    msg=MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email,from_password)
    gmail.send_message(msg)
