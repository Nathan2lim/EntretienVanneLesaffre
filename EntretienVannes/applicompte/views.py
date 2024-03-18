from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

from appliVanne.models import *




# Create your views here.
def connexion(request):
    user = None

    if not request.user.is_authenticated:
        usr = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(request, username = usr, password = pwd)
        if user is not None:
            login(request, user)

            lesVanne = Vanne.objects.all()

            return redirect('vannes')

        else :
            return render(
                request,
                'applicompte/login.html'
            )

    else :
        return render(
            request,
            'applicompte/login.html'
        )

def deconnexion(request):
    logout(request)
    return render(
        request,
        'applicompte/logout.html'
    )
