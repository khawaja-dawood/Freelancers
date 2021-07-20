from django.urls import path
from . import views


urlpatterns = [
    path('', views.Projects, name='Projects'),
    path('project/<str:pk>/', views.Project, name='Project')
]