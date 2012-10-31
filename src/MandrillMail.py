import os
import smtplib
import mimetypes
import string

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email import encoders

def attachFiles(message,filepaths):
    for filename in filepaths:
        if not os.path.isfile(filename):
            print 'NO SUCH FILE: ',filename
            continue
        print filename
        contentType, encoding = mimetypes.guess_type(filename)
        if contentType is None or encoding is not None:
            #No guess could be made or the file is encoded/compressed, treat it as binary
            contentType = 'application/octet-stream' 
        maintype, subtype = contentType.split('/')
        if maintype == 'text':
            f = open(filename,'r')
            #for generality, check the charset being used
            attachment = MIMEText(f.read(),_subtype=subtype)
        else:
            f = open(filename,'rb')
            if maintype == 'image':
                attachment = MIMEImage(f.read(),_subtype=subtype)
            elif maintype == 'audio':
                attachment = MIMEAudio(f.read(),_subtype=subtype)
            else:
                attachment = MIMEBase(maintype,subtype)
                attachment.set_payload(f.read())
                encoders.encode_base64(attachment)
        attachment.add_header('Content-Disposition','attachment', filename=filename)
        f.close()
        message.attach(attachment)

def loadMessageTemplate(filename,msgType = 'html'):
    f = open(filename,'r')
    msgbody = f.read()
    message = MIMEText(msgbody,msgType)
    f.close()
    return message

def loadMessageRecipients(filename):
    f = open(filename,'r')
    recipients = [recipient.strip() for recipient in f]
    f.close()
    return recipients

def loadAttachmentList(filename):
    f = open(filename,'r')
    attachments = [attachment.strip() for attachment in f]
    f.close()
    return attachments

def sendMessageSMTP(server,auth,sender,recipient_src,subject,template_src,attachment_src):    
    assert type(server) == tuple
    assert type(auth) == tuple
    
    msg = MIMEMultipart()
    
    msg['From'] = sender #sender_name<email_address>
    
    recipients = loadMessageRecipients(recipient_src)
    
    msg['Subject'] = subject
    
    body = loadMessageTemplate(template_src)
    msg.attach(body)
    
    attachments = loadAttachmentList(attachment_src)
    attachFiles(msg,attachments)
    host = server[0]
    port = server[1]
    s = smtplib.SMTP(host,port)
    if auth:
        username = auth[0]
        password = auth[1]
        s.login(username,password)
    s.set_debuglevel(False) # show communication with the server if true
    try:
        s.sendmail(msg['From'],recipients,msg.as_string())
    finally:
        s.quit()