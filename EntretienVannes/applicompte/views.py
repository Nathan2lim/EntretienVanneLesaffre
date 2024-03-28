from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

from appliVanne.models import *


from django.views.decorators.http import require_http_methods
from django.contrib import messages



# Create your views here.
def connexion(request):

    if request.user.is_authenticated:
            return redirect('vannes')
    else:
        usr = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(request, username=usr, password=pwd)
        if user is not None:
            login(request, user)
            return redirect('vannes')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
            return redirect('login')

def deconnexion(request):
    logout(request)
    return render(
        request,
        'applicompte/logout.html'
    )
