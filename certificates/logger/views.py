from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from author.models import UserSettings
from .models import Logger

# Create your views here.

@login_required(login_url='/account/')
def loggerPage(request):

    try:
        logs = Logger.objects.order_by('-primary')[:1000]
    except:
        logs = Logger.objects.order_by('-primary')

    # settings
    author = str(request.user)
    userSettings = UserSettings.objects.get(author=author)

    response = {
        'logs'        : logs,
        'userSettings': userSettings
    }

    return render(request, 'dashboard/logger.html', response)

