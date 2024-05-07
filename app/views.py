from django.shortcuts import render
from django.core.mail import send_mail
import smtplib
# Create your views here.
def home(request):
        
    email_sent =send_mail(
        'Subject here',
        'Here is the message.',
        'armaan@theskytrails.com',
        ['armaanalamf65@gmail.com'],
        fail_silently=False,
    )
    if email_sent == 1:
        # Email sent successfully
        print("Email sent successfully")
    else:
        # Handle failure to send email
        print("Failed to send email")
    return render(request,'home.html')
