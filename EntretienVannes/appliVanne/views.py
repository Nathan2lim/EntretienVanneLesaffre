from django.shortcuts import render
from appliVanne.models import Vanne
from appliVanne.models import Vanne, ACTIONNEUR, CORPS, POSITIONNEUR, TYPEPOSITIONNEUR, FOURNISSEUR

# Create your views here.


#affichage des vannes 
def vannes(request) :
    LesVannes = Vanne.objects.all() 
    return render(request, "appliVanne/vannes.html", {"vannes": LesVannes})

def listeVanne (request):
    lesVannes  = Vanne.objects.all()
    return render(request, "appliVanne/vannes.html", {"listeVannes": lesVannes})


    
    
    
    
