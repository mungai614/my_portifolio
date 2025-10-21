from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

# views.py in your Django app

from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message_body = request.POST.get('message')

        # Compose email content
        subject = "New Contact Form Submission"
        message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message_body}"
        from_email = settings.DEFAULT_FROM_EMAIL  # Usually same as EMAIL_HOST_USER
        recipient_list = ['jeremynjango2@gmail.com']  # Change to your real email

        # Send the email
        try:
            send_mail(subject, message, from_email, recipient_list)
            messages.success(request, f"Thanks {name}, your message has been sent successfully.")
        except Exception as e:
            messages.error(request, f"Sorry, an error occurred: {e}")

        return redirect('home')

