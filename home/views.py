from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime


# Create your views here.

current_date = datetime.now().strftime("%Y")


def index(request):
    return render(request, "home/index.html", {'current_date': current_date})



def contact(request):       
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            number = form.cleaned_data['number']
            from_email = settings.DEFAULT_FROM_EMAIL
            
        
            # Forward the message to the admin email
            message += f'\n\nFrom: {name}\nNumber: {number}\nEmail: {email}'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [settings.ADMIN_EMAIL]
            
            send_mail(subject, message, from_email, recipient_list)
            
            messages.success(request, 'Mesajınız başarılı bir şekilde iletildi. En kısa zamanda size dönüş yaparız!')
            return redirect('home:contact')
    else:
        form = ContactForm()

    return render(request, "home/contact.html", {'form': form, 'current_date': current_date})