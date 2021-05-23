
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from author.models import UserSettings
# Create your views here.

@login_required(login_url='/account/')
def dashboardPage(request):

    author = str(request.user)
    settings = UserSettings.objects.get(id=request.user.id)

    response = {
        'settings' : settings
    }
    return render(request, 'dashboard/Dashboard.html', response)
