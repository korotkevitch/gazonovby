from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.views import View
from .models import Gallery, Head, About, Service, Testimonial, Contact
from .forms import UserForm
from django.core.mail import BadHeaderError
from django.views.generic.edit import FormView
from django.core.mail import send_mail


class IndexView(ListView):
    model = Gallery
    template_name = 'index.html'
    context_object_name = 'gallery'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['head'] = Head.objects.all()
        context['about'] = About.objects.all()
        context['service'] = Service.objects.all()
        context['testimonials'] = Testimonial.objects.all()
        return context


class ContactView(FormView):
    model = Contact
    form_class = UserForm
    success_url = '/thanks'

    def form_valid(self, myform):
        myform.send_mail()
        myform.save()  # сохранение в БД
        return super().form_valid(myform)


class ThanksView(IndexView):
    model = Gallery
    template_name = 'thanks.html'
    context_object_name = 'gallery'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context
