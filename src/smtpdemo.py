import os
import MandrillMail
        

def main():
    print 'SWOOP'
    
    #for testing on the local host
    #host = '127.0.0.1'
    #port = 8025
    host = 'smtp.mandrillapp.com'
    port = 587
    server = (host,port)
    
    username = os.environ['MANDRILL_USERNAME']
    password = os.environ['MANDRILL_PASSWORD']
    auth = (username,password)
    
    sender = 'Cesar Flores <cgonzalezflores1@gmail.com>' #sender_name<email_address>
    recipient_src = 'recipients.txt'
    subject = 'HEYYY, SEXY MONKEY'
    template_src = 'HTemailtemplate.html'
    attachment_src = 'attachments.txt'
    
    MandrillMail.sendMessageSMTP(server, auth, sender, recipient_src, subject, template_src, attachment_src)
    print 'SWAG'

if __name__ == "__main__":
    main()