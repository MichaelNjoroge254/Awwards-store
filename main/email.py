from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(name,receiver,date):
    # Creating message subject and sender
    subject = 'Welcome to the Awwwards clone'
    sender = 'testmugera@gmail.com'
    ctx= {
        "name": name,
       "date":date
    }


    #passing in the context vairables
    text_content = render_to_string('email/awwemail.txt',ctx)
    html_content = render_to_string('email/awwemail.html',ctx)

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()