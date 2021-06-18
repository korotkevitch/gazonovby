from django import forms
from django.core.mail import send_mail as django_send_mail
from django.forms import ModelForm
from .models import Contact

class UserForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'  # вместо перечисления всех полей: fields = ['name', 'phone', 'message']

    def send_mail(self):
        return django_send_mail('Сообщение с сайта gazonov.by',
                    str('Имя: ') + self.cleaned_data['name'] + '\n' + str('Телефон: ') + self.cleaned_data['phone'] + '\n' + str('Сообщение: ') + self.cleaned_data['message'],
                    'no-reply@gazonov.by',
                    ['info@iko-studio.com'])
