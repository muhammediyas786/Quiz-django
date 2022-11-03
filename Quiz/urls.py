from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('questions/<str:category>/<int:number>/',questions_method,name='questions'),
]
