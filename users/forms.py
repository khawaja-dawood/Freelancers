from django import forms
from django.contrib.auth.forms import UserCreationForm

from projects.models import MyUser


# class RegisterForm(UserCreationForm):
#
#     class meta:
#         model = MyUser
#         fields = '__all__'
#         exclude = ['user_role', 'is_staff', 'is_active', 'tags']