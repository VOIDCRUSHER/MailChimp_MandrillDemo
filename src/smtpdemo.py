import os
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.Utils import COMMASPACE
from email import Encoders

def attachFiles(message,filepaths):
    for file in filepaths:
        attachment = MIMEBase('application',"octet-stream")
        attachment.set_payload(open(file,'rb').read())
        Encoders.encode_base64(attachment)
        attachment.add_header('Content-Disposition','attachment; filename="%s"'%os.path.basename(file))
        message.attach(attachment)

def loadMessageTemplate(filename,msgType = 'html'):
    f = open(filename,'r')
    msgbody = f.read()
    message = MIMEText(msgbody,msgType)
    return message

def loadMessageRecipients(filename):
    f = open(filename,'r')
    recipients = [recipient for recipient in f]
    return recipients
        

def main():
    print 'SWOOP'
    msg = MIMEMultipart('alternative')
    
    msg['Subject'] = 'Oppa Mandrill Style!'
    msg['From'] = 'Cesar Flores <cgonzalezflores1@gmail.com>' #sender_name<email_address>
    msg['To'] = ['cgonzalez6@gatech.edu']
    
    text = "Heyyy Sexy Raaady! (Plaintext Example)"
    part1 = MIMEText(text,'plain')
    
    html = '<em>You know what Im <strong>sayin</strong></em>(HTML Demo)'
    part2 = MIMEText(html,'html')
    
    username = os.environ['MANDRILL_USERNAME']
    password = os.environ['MANDRILL_PASSWORD']
    
    msg.attach(part1)
    msg.attach(part2)
    
    s = smtplib.SMTP('smtp.mandrillapp.com',587)
    
    s.login(username,password)
    s.sendmail(msg['From'],msg['To'],msg.as_string())
    
    s.quit()
    print 'SWAG'

if __name__ == "__main__":
    main()