from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

# views.py in your Django app

from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt  # disable CSRF for simplicity; better to use tokens or allow from frontend properly
def contact(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            message_body = data.get('message')

            if not name or not email or not message_body:
                return JsonResponse({'error': 'Please fill in all fields.'}, status=400)

            subject = "New Portfolio Contact Form Message"
            message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message_body}"
            recipient_list = ['your-email@gmail.com']  # your email here

            send_mail(subject, message, email, recipient_list)
            return JsonResponse({'message': 'Message sent successfully!'})
        except Exception as e:
            print(f"Error sending email: {e}")
            return JsonResponse({'error': 'Failed to send email.'}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=405)
