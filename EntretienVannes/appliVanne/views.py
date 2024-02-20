from django.shortcuts import render
from appliVanne.models import Vanne
from appliVanne.models import Vanne, ACTIONNEUR, CORPS, POSITIONNEUR, TYPEPOSITIONNEUR, FOURNISSEUR
from django.http import JsonResponse
from django.core import serializers
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
# Create your views here.


#affichage des vannes 
def vannes(request) :
    LesVannes = Vanne.objects.all() 
    return render(request, "appliVanne/vannes.html", {"vannes": LesVannes})

def positionneur(request) :
    LesPositionneur = POSITIONNEUR.objects.all() 
    return render(request, "appliVanne/positionneur.html", {"listePos": LesPositionneur})

def actionneur(request) :
    LesActionneurs = ACTIONNEUR.objects.all() 
    return render(request, "appliVanne/actionneur.html", {"listeAct": LesActionneurs})


def listeVanne(request):
    tri = request.GET.get('tri', 'id_vanne')  # Le champ par défaut pour le tri
    ordre = request.GET.get('ordre', 'desc')
    
    if ordre == 'asc':
        tri = f'-{tri}'
    
    print(f'Tri : {tri}, Ordre : {ordre}')
    
    lesVannes = Vanne.objects.all().order_by(tri).filter(en_service_vanne=1)

    return render(request, "appliVanne/vannes.html", {"listeVannes": lesVannes})

def rechercheVanne(request):
    if request.method == 'GET':
        search_query = request.GET.get('term', '')
        query = Q(id_vanne__icontains=search_query) | \
                Q(id_atelier__nom_atelier__icontains=search_query) | \
                Q(repere_vanne__icontains=search_query) | \
                Q(affectation_vanne__icontains=search_query) | \
                Q(type_vannes__icontains=search_query) | \
                Q(voir_en__icontains=search_query) | \
                Q(id_positionneur__fonctionnement_positionneur__description_type_positionneur__icontains=search_query)
                
        if search_query.isdigit():
            query |= Q(en_service_vanne=int(search_query))

        vannes = Vanne.objects.filter(query).values('id_vanne', 'id_atelier__nom_atelier', 'repere_vanne', 'affectation_vanne', 'type_vannes', 'voir_en', 'en_service_vanne', 'id_positionneur__fonctionnement_positionneur__description_type_positionneur')

        response_data = {
            'results': list(vannes),
            'status': 'OK'
        }

        return JsonResponse(response_data, safe=False)
    else:
        return JsonResponse({'error': 'Méthode non autorisée'}, status=405)

    
def rechercheAJAX(request):
    
        return render(request, "appliVanne/vanneAJAX.html")
    

def detailVanne(request, id_vanne):
    vanne = Vanne.objects.get(id_vanne=id_vanne)
    return render(request, "appliVanne/detailVanne.html", {"vanne": vanne})


def formulaireAjoutVanne(request): 

    return render(
            request,
            'appliVanne/creationVanne.html',
        )
    
def historiqueVanne(request):
    LesVannes = Vanne.objects.filter(en_service_vanne=0)
    return render(request, "appliVanne/historique.html", {"listeVannes": LesVannes})

def delete(request, id_vanne):
    vanne = get_object_or_404(Vanne, id_vanne=id_vanne)
    vanne.en_service_vanne = 0
    vanne.save() 
    
    return redirect('historique')

def recover(request, id_vanne):
    vanne = get_object_or_404(Vanne, id_vanne=id_vanne)
    vanne.en_service_vanne = 1
    vanne.save() 
    return redirect('vannes')


