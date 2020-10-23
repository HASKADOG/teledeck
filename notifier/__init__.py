import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(to, mesg):
    msg = MIMEMultipart()

    to_email = to
    message = mesg

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.timeweb.ru:2525')
    server.login('teledoska@369525-ct08796.tmweb.ru', 'qwe123qwe123')



    server.sendmail('teledoska@369525-ct08796.tmweb.ru', to_email, msg.as_string())
    server.quit()