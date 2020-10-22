import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

msg = MIMEMultipart()

to_email = 'cplasplas16@gmail.com'
message = 'IS THIS A real life&'

msg.attach(MIMEText(message, 'plain'))

server = smtplib.SMTP('smtp.timeweb.ru:2525')
server.login('teledoska@369525-ct08796.tmweb.ru', 'qwe123qwe123')
server.sendmail('teledoska@369525-ct08796.tmweb.ru', to_email, msg.as_string())