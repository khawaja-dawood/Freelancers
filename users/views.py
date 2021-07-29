from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
# Create your views here.



# class CustomLoginView(LoginView):
#     form_class = AuthenticationForm
#     template_name = 'users/login.html'
#
#     def my_login(self, request):
#         if request.user.is_authenticated():
#             return redirect("projects-home")
#         else:
#             return login(request, 'template/login.html')

