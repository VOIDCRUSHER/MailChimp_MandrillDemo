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

def loadAttachmentList(filename):
    f = open(filename,'r')
    attachments = [attachment for attachment in f]
    return attachments

def sendMessageSMTP(username,password,sender,recipient_src,subject,template_src,attachment_src):    
    msg = MIMEMultipart()
    
    msg['From'] = sender #sender_name<email_address>
    
    recipients = loadMessageRecipients(recipient_src)
    msg['To'] = COMMASPACE.join(recipients)
    
    msg['Subject'] = subject
    
    body = loadMessageTemplate(template_src)
    msg.attach(body)
    
    attachments = loadAttachmentList(attachment_src)
    attachFiles(msg,attachments)
            
    s = smtplib.SMTP('smtp.mandrillapp.com',587)
    
    s.login(username,password)
    s.sendmail(msg['From'],msg['To'],msg.as_string())
    
    s.quit()