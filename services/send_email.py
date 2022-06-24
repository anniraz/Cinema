from email.mime.text import MIMEText
import smtplib

from .keys import recipient

def send_email(name,email,messege,password):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()

    messege = f'My name is {name}\n {messege}'


    try:
        server.login(email,password)
        msg=MIMEText(messege)
        msg['From']=email
        msg['To']=recipient
        server.sendmail(email,recipient,msg.as_string())


    except Exception as ex :
        return f'{ex}\nCheck your login or password!'