from django.shortcuts import render
from django.http import HttpResponse

from .forms import ContactForm # Add this
from django.core.mail import send_mail
from django.contrib import messages
from django.http import JsonResponse

from django.contrib import messages

import pytz
from datetime import datetime


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']

            message = "{0} - {1} has sent you a new message:\n\n{2}".format(sender_name, sender_email, form.cleaned_data['message'])
            send_mail('New Enquiry', message, sender_email, ['eamanu@yaerobi.com'], fail_silently=False)

            messages.success(request, "Message sent successfully. We will contact you soon. Thanks!")


            return render(request, 'website/home.html')
    else:
        form = ContactForm()
    
    return render(request, 'website/home.html', {'form': form})


def get_time(request):
    if request.method == 'GET':
        tz = pytz.timezone('America/Argentina/Buenos_Aires')
        ct = datetime.now(tz=tz)

        return JsonResponse({'currentDateTime': ct.isoformat()})
