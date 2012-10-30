import os
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def main():
    print 'SWOOP'
    msg = MIMEMultipart('alternative')
    
    msg['Subject'] = 'Oppa Mandrill Style!'
    msg['From'] = 'Cesar Flores <cgonzalezflores1@gmail.com>' #sender_name<email_address>
    msg['To'] = 'cgonzalez6@gatech.edu'
    
    text = "Heyyy Sexy Raaady! (Plaintext Example)"
    part1 = MIMEText(text,'plain')
    
    html = '<em>You know what Im <strong>sayin</strong></em>(HTML Demo)'
    part2 = MIMEText(html,'html')
    
    username = os.environ['MANDRILL_USERNAME']
    password = os.environ['MANDRILL_PASSWORD']
    
    msg.attach(part1)
    #msg.attach(part2)
    
    s = smtplib.SMTP('smtp.mandrillapp.com',587)
    
    s.login(username,password)
    s.sendmail(msg['From'],msg['To'],msg.as_string())
    
    s.quit()
    print 'SWAG'

if __name__ == "__main__":
    main()