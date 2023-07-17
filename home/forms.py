from django import forms
from django.core.validators import RegexValidator



class ContactForm(forms.Form):
    name = forms.CharField(label='İsim & Soyisim', max_length=100)
    email = forms.EmailField(label='Email')
    subject = forms.CharField(label='Konu', max_length=150)
    number = forms.CharField(
        validators=[
            RegexValidator(
                regex=r'^[0-9]{11}$',  # Define the desired pattern using a regular expression
                message='Geçerli bir telefon numara giriniz. 05xx xxx xx xx'
            )
        ],
        label='Telefon No'
    )
    message = forms.CharField(label='Mesajınız', widget=forms.Textarea)
