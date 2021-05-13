
from django.conf import settings
from django.urls import path, include
# import views from application
from .views import *

urlpatterns = [
    path('graduates/', graduatesView, name='graduatesView'),
    path('addStudent/', addStudent, name='addStudent'),
    path('studentProfile/<int:pk>/', studentProfile, name='studentProfile'),
    path('printPage/<int:pk>/', printPage, name='printPage'),
]
