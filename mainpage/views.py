from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Project, Tag
from .forms import ContactForm


def home(request):
  
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      name= form.cleaned_data.get("name")
      email= form.cleaned_data.get("email")
      message=form.cleaned_data.get("message")
      
      comment = f"Incoming message from {name}. The message is as stated below. \n\n" + message;
      send_mail('New Enquiry', comment, email, ['noreplaymail84@gmail.com'])

      messages.add_message(request, messages.SUCCESS, "Your message has been sent.")

      return redirect('home')
  else: 
    form = ContactForm()

  projects = Project.objects.all()
  context ={
    'form':form,
    'projects': projects
  }

  return render(request, 'mainpage/main.html', context )

# def success(request):
#   message = 'Thank you for your message'

#   return render(request, 'mainpage/test.html', {'message':message})
