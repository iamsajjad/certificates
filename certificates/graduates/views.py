
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/account/')
def graduatesView(request):

    response = {
        'name' : "aaa"
    }

    return render(request, 'graduates/Graduates.html', response)
