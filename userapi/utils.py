from django.core.mail import send_mail
from django.conf import settings

def send_email(username, email):
    subject = 'Welcome to New Yale User'
    body = f'''
               Hello {username}! your registration is successful.
            '''
    send_mail(
        subject,
        body,
        settings.EMAIL_HOST_USER,
        [email], 
        fail_silently=False    
    )