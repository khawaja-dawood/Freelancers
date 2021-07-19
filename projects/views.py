from django.shortcuts import render
from django.http import HttpResponse



def projects(request):
    return render(request=request, template_name='projects/projects.html')


def project(request, pk):
    return render(request=request, template_name='projects/single-project.html')