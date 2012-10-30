import os
import MandrillMail
        

def main():
    print 'SWOOP'
    
    username = os.environ['MANDRILL_USERNAME']
    password = os.environ['MANDRILL_PASSWORD']
    
    sender = 'Cesar Flores <cgonzalezflores1@gmail.com>' #sender_name<email_address>
    recipient_src = 'recipients.txt'
    subject = 'HEYYY, SEXY MONKEY'
    template_src = 'HTemailtemplate.txt'
    attachment_src = 'attachments.txt'
    
    MandrillMail.sendMessageSMTP(username, password, sender, recipient_src, subject, template_src, attachment_src)
    print 'SWAG'

if __name__ == "__main__":
    main()