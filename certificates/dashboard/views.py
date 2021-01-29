
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/account/')
def dashboardPage(request):
    response = {
        'name' : "aaa"
    }
    return render(request, 'dashboard/Dashboard.html', response)
