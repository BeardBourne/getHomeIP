import urllib.request
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

while True:
    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    mail_content = external_ip
    #The mail addresses and password
    sender_address = 'your-address@gmail.com'
    sender_pass = 'your-password'
    receiver_address = 'your-receiver-address@gmail.com'
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'External IP of Home!'   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')
    time.sleep(3600)