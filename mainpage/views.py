from django.shortcuts import render
from .models import Project, Tag


def home(request):

  projects = Project.objects.all()


  return render(request, 'mainpage/main.html', {'projects': projects})
