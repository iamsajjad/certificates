
from django.conf import settings
from django.urls import path, include
# import views from application
from .views import *

urlpatterns = [
    path('', dashboardPage),
    path('dashboard/', dashboardPage, name='dashboardPage'),
]
