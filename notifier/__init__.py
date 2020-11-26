import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(to, mesg, subj):
    msg = MIMEMultipart()

    to_email = to
    message = mesg

    msg['Subject'] = subj

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.timeweb.ru:2525')
    server.login('teledoska@xn--80ahca0adxyd.xn--p1ai', 'TeledeckEfir24')



    server.sendmail('teledoska@xn--80ahca0adxyd.xn--p1ai', to_email, msg.as_string())
    server.quit()