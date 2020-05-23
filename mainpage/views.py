from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Project, Tag
from .forms import ContactForm


def home(request):

  # if request.method == 'POST':
  #   form = ContactForm(request.POST)
  #   if form.is_valid():
  #     return HttpResponse('Thanks you for your message')
  # else: 
  form = ContactForm()

  projects = Project.objects.all()
  context ={
    'form':form,
    'projects': projects
  }


  return render(request, 'mainpage/main.html', context)
