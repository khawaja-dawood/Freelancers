from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView

from django.views.generic import CreateView
# Create your views here.


def userProfile(request, pk):

    return render(request=request, template_name='users/user-profile.html')


