from django.shortcuts import render
from appliVanne.models import Vanne
from appliVanne.models import Vanne, ACTIONNEUR, CORPS, POSITIONNEUR, TYPEPOSITIONNEUR, FOURNISSEUR
from django.http import JsonResponse
from django.core import serializers
from django.db.models import Q
# Create your views here.


#affichage des vannes 
def vannes(request) :
    LesVannes = Vanne.objects.all() 
    return render(request, "appliVanne/vannes.html", {"vannes": LesVannes})

def positionneur(request) :
    LesPositionneur = POSITIONNEUR.objects.all() 
    return render(request, "appliVanne/positionneur.html", {"listePos": LesPositionneur})


def listeVanne(request):
    tri = request.GET.get('tri', 'id_vanne')  # Le champ par défaut pour le tri
    ordre = request.GET.get('ordre', 'desc')
    
    if ordre == 'asc':
        tri = f'-{tri}'
    
    print(f'Tri : {tri}, Ordre : {ordre}')
    
    lesVannes = Vanne.objects.all().order_by(tri)
    return render(request, "appliVanne/vannes.html", {"listeVannes": lesVannes})

def rechercheVanne(request):
    if request.method == 'GET':
        search_query = request.GET.get('term', '')  # Récupérez le paramètre de recherche 'term'
        # Effectuez la recherche dans le modèle Vanne en fonction du terme de recherche
        vannes = Vanne.objects.filter(
            Q(id_vanne__icontains=search_query) |
            Q(id_atelier__nom_atelier__icontains=search_query) |
            Q(repere_vanne__icontains=search_query) |
            Q(affectation_vanne__icontains=search_query) |
            Q(type_vannes__icontains=search_query)|
            Q(voir_en__icontains=search_query)
        ).values('id_vanne', 'id_atelier__nom_atelier', 'repere_vanne', 'affectation_vanne', 'type_vannes', 'voir_en')

        # Ajoutez la vérification supplémentaire "OK" à la réponse JSON
        response_data = {
            'results': list(vannes),
            'status': 'OK'
        }

        # Renvoyez les résultats de la recherche sous forme de réponse JSON avec la vérification supplémentaire
        return JsonResponse(response_data, safe=False)
    else:
        # Si la méthode de la requête n'est pas GET, renvoyez une réponse d'erreur
        return JsonResponse({'error': 'Méthode non autorisée'}, status=405)
    
    
def rechercheAJAX(request):
    
        return render(request, "appliVanne/vanneAJAX.html")
    

def detailVanne(request, id_vanne):
    vanne = Vanne.objects.get(id_vanne=id_vanne)
    return render(request, "appliVanne/detailVanne.html", {"vanne": vanne})
