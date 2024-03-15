import datetime
import re
from django.shortcuts import render
from appliVanne.models import *
from applicompte.models import *
from appliVanne.forms import *
from django.http import JsonResponse
from django.core import serializers
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from datetime import datetime
from django.forms import formset_factory
from .forms import CommentForm
# Create your views here.


#affichage des vannes 
def vannes(request) :
    LesVannes = Vanne.objects.all() 
    return render(request, "appliVanne/vannes.html", {"vannes": LesVannes})

def rechangeREG(request) :
    lesVannes = Vanne.objects.all().filter(en_service_vanne=2)
    return render(request, "appliVanne/rechangeREG.html", {"listeVanne": lesVannes})

def rechangeTOR(request) :
    lesVannes = Vanne.objects.all().filter(en_service_vanne=3)
    return render(request, "appliVanne/rechangeTOR.html", {"listeVanne": lesVannes})

def actionneur(request) :
    LesActionneurs = ACTIONNEUR.objects.all() 
    return render(request, "appliVanne/actionneur.html", {"listeAct": LesActionneurs})

def listeVanne(request):
    tri = request.GET.get('tri', 'id_vanne')  # Le champ par défaut pour le tri
    ordre = request.GET.get('ordre', 'desc')
    
    if ordre == 'asc':
        tri = f'-{tri}'
    
    #print(f'Tri : {tri}, Ordre : {ordre}')
    
    lesVannes = Vanne.objects.all().order_by(tri).filter(en_service_vanne=1)

    return render(request, "appliVanne/vannes.html", {"listeVannes": lesVannes})

def rechercheVanne(request):
    if request.method == 'GET':
        # Je récupère plusieurs données sous term[] avec term[] : 'niveau' et term[] : 'reg'
        search_queries = request.GET.getlist('term[]')
        vannes = Vanne.objects.all() 
        

        for query_str in search_queries:
            #print('Query: ' + query_str)
            query = Q(id_vanne__icontains=query_str) | \
                    Q(id_atelier__nom_atelier__icontains=query_str) | \
                    Q(repere_vanne__icontains=query_str) | \
                    Q(affectation_vanne__icontains=query_str) | \
                    Q(type_vannes__icontains=query_str) | \
                    Q(voir_en__icontains=query_str) | \
                    Q(id_corps__dn_corps__icontains=query_str) | \
                    Q(id_positionneur__fonctionnement_positionneur__description_type_positionneur__icontains=query_str)
                    
            if query_str.isdigit():
                query |= Q(en_service_vanne=int(query_str))

            vannes = vannes.filter(query)

        vannes = vannes.values(
            'id_vanne', 'id_atelier__nom_atelier', 'repere_vanne',
            'affectation_vanne', 'type_vannes', 'voir_en',
            'en_service_vanne','id_corps__dn_corps', 'id_positionneur__fonctionnement_positionneur__description_type_positionneur'
        )

        response_data = {
            'results': list(vannes),
            'status': 'OK'
        }

        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Méthode non autorisée'}, status=405)

def rechercheAJAX(request):
    
        return render(request, "appliVanne/vanneAJAX.html")

def detailVanne(request, id_vanne):
    vanne = Vanne.objects.get(id_vanne=id_vanne)
    infoRev = REVISON.objects.filter(rev_id_vanne=id_vanne)

    return render(request, "appliVanne/detailVanne.html", {"vanne": vanne, "infoRevision":infoRev })

def formulaireAjoutVanne(request): 
    if request.user.is_authenticated:
        
        return render(
                request,
                'appliVanne/creationVanne.html',
            )
    else:
        redirect('login')

def historiqueVanne(request):
    LesVannes = Vanne.objects.filter(en_service_vanne=0)
    lesREv = REVISON.objects.all().order_by('-id_revision')
    return render(request, "appliVanne/historique.html", {"listeVannes": LesVannes, "listeRev": lesREv})

def delete(request, id_vanne):
    if request.user.is_authenticated:
        vanne = get_object_or_404(Vanne, id_vanne=id_vanne)
        vanne.en_service_vanne = 0
        vanne.save()

        rev = REVISON(
            rev_id_vanne=id_vanne,
            date_revision=datetime.now(),
            id_revision_vanne = numRev(id_vanne),
            type_revision = "Suppression",
            commentaire_revision="Suppression de la vanne",
            nom_technicien = request.user.first_name + " " + request.user.last_name

        )
        
        rev.full_clean()
        rev.save()
        
        return redirect('vannes')
    else:
        return redirect('login')

def rechange(request, id_vanne):
    if request.user.is_authenticated:

        vanne = get_object_or_404(Vanne, id_vanne=id_vanne)
        atelierREG = ATELIER.objects.get(nom_atelier="Rechange REG")
        atelierTOR = ATELIER.objects.get(nom_atelier="Rechange TOR")
        infoRev = REVISON.objects.filter(rev_id_vanne=id_vanne).last()

        
        if vanne.repere_vanne != None and vanne.affectation_vanne != None:
            com = "Rechange de la vanne, sont affectation et son repère ont été supprimés, ils étaient : " + vanne.repere_vanne + " et " + vanne.affectation_vanne 
        elif vanne.repere_vanne != None:
            com = "Rechange de la vanne, son repère a été supprimé, il était : " + vanne.repere_vanne
        elif vanne.affectation_vanne != None:
            com = "Rechange de la vanne, son affectation a été supprimée, elle était : " + vanne.affectation_vanne
        else:
            com = "Rechange de la vanne"

        if vanne.type_vannes == 'TOR':
            vanne.id_atelier = atelierTOR
            vanne.en_service_vanne = 3
        else:
            vanne.id_atelier = atelierREG
            vanne.en_service_vanne = 2
        vanne.repere_vanne = None
        vanne.affectation_vanne = None
        vanne.numero_commande = None
        vanne.save() 
        

        rev = REVISON(
            rev_id_vanne=id_vanne,
            date_revision=datetime.now(),
            id_revision_vanne = numRev(id_vanne),
            type_revision = "Rechange",
            commentaire_revision=com,
            nom_technicien = request.user.first_name + " " + request.user.last_name

        )
        rev.full_clean()
        rev.save()
        
        return redirect('vannes')
    else :
        return redirect('login')

def recover(request, id_vanne):
    if request.user.is_authenticated:
        
        vanne = get_object_or_404(Vanne, id_vanne=id_vanne)
        vanne.en_service_vanne = 1
        vanne.voir_en 
        vanne.save() 
        
        rev = REVISON(
            rev_id_vanne=id_vanne,
            date_revision=datetime.now(),
            id_revision_vanne = numRev(id_vanne),
            type_revision = "Reprise",
            commentaire_revision="Reprise de la vanne",
            nom_technicien = request.user.first_name + " " + request.user.last_name

        )
        rev.full_clean()
        rev.save()

        if vanne.id_atelier.id_atelier == 12 or vanne.id_atelier.id_atelier == 13:
            return redirect('edit', id_vanne) 
        return redirect('vannes')
    else:
        return redirect('login')
    
def recoverBIS(request, id_vanne):
    if request.user.is_authenticated:
        vanne = get_object_or_404(Vanne, id_vanne=id_vanne)
        vanne.en_service_vanne = 1
        vanne.save() 
        
        rev = REVISON(
            rev_id_vanne=get_object_or_404(Vanne, id_vanne=id_vanne),
            date_revision=datetime.now(),
            id_revision_vanne = numRev(id_vanne),
            type_revision = "Reprise",
            commentaire_revision="Reprise de la vanne",
            nom_technicien = request.user.first_name + " " + request.user.last_name

        )
        rev.full_clean()
        rev.save()
        return edit(request, id_vanne)
    else:
        return redirect('login')

def ajoutVanne(request):
    if request.user.is_authenticated: 
        LesVannes  = Vanne.objects.all()
        LesAtelier  = ATELIER.objects.all()
        lesFournisseur = FOURNISSEUR.objects.all() 
        typePos = TYPEPOSITIONNEUR.objects.all()
        
        return render(request, "appliVanne/creationVanne.html", {"listVannes": LesVannes, "listAtelier": LesAtelier, "listFournisseur": lesFournisseur, "listTypePos": typePos})
    else:
        return redirect('login')
    
def traitementAjoutVanne(request):
    if request.user.is_authenticated:

        save = True
        
        LesVannes = Vanne.objects.all().order_by('-id_vanne').filter(en_service_vanne=1)
        LesAtelier  = ATELIER.objects.all()
        lesFournisseur = FOURNISSEUR.objects.all() 
        typePos = TYPEPOSITIONNEUR.objects.all()
        
        
        if request.method == "POST":
            form = VanneForm(request.POST)
            now = datetime.now()


            if form.is_valid():
                
                
                
                num_atelier = form.cleaned_data['id_atelier']
                nouveau_atelier = form.cleaned_data['nouveau_atelier']
                
                num_fournisseur = form.cleaned_data['id_fournisseur']
                nouveau_fournisseur = form.cleaned_data['nouveau_fournisseur']
                
                num_fournisseur_actionneur = form.cleaned_data['id_fournisseur_actionneur']
                nouveau_fournisseur_actionneur = form.cleaned_data['nouveau_fournisseur_actionneur']
                
                tempsRev = form.cleaned_data['tempsRev']
                
                #CORPS
                taille_corps = form.cleaned_data['taille_corps']
                code_corps = form.cleaned_data['code_corps']
                type_corps = form.cleaned_data['type_corps']
                pn_corps = form.cleaned_data['pn_corps']
                cv_corps = form.cleaned_data['cv_corps']
                numero_serie_corps = form.cleaned_data['numero_serie_corps']
                corps_corps = form.cleaned_data['corps_corps']
                norme_bride_corps = form.cleaned_data['norme_bride_corps']
                garniture_corps = form.cleaned_data['garniture_corps']
                type_garniture = form.cleaned_data['type_garniture']
                matiere_arbre = form.cleaned_data['matiere_arbre']
                matiere_siege = form.cleaned_data['matiere_siege']
                matiere_organe_reglant = form.cleaned_data['matiere_organe_reglant']
                
                

                #ACTIONNEUR
                taille_actionneur = form.cleaned_data['taille_actionneur']
                type_actionneur = form.cleaned_data['type_actionneur']
                numero_serie_actionneur = form.cleaned_data['numero_serie_actionneur']
                commande_manuelle_actionneur = form.cleaned_data['commande_manuelle_actionneur']
                sens_actionneur = form.cleaned_data['sens_actionneur']
                pression_alimentation = form.cleaned_data['pression_alimentation']
                type_contact = form.cleaned_data['type_contact']
                type_effet = form.cleaned_data['type_effet']
                type_contact_actionneur = form.cleaned_data['type_contact_actionneur']
                
                #POSITIONNEUR
                num_fournisseur_positionneur = form.cleaned_data['id_fournisseur_positionneur']
                nouveau_fournisseur_positionneur = form.cleaned_data['nouveau_fournisseur_positionneur']
                id_fonctionnement_positionneur = form.cleaned_data['id_fonctionnement_positionneur']
                type_positionneur = form.cleaned_data['type_positionneur']
                numero_serie_positionneur = form.cleaned_data['numero_serie_positionneur']
                signal_sortie_positionneur = form.cleaned_data['signal_sortie_positionneur']
                signal_entree_positionneur = form.cleaned_data['signal_entree_positionneur']
                repere_came_positionneur = form.cleaned_data['repere_came_positionneur']
                face_came_positionneur = form.cleaned_data['face_came_positionneur']
                sens_action = form.cleaned_data['sens_action']
                fermee_a_positionneur = form.cleaned_data['fermee_a_positionneur']
                ouverte_a_positionneur = form.cleaned_data['ouverte_a_positionneur']
                pression_alimentation_positionneur = form.cleaned_data['alimentation_positionneur']
                loi_pos = form.cleaned_data['loi_commande_positionneur']
                
                presence_positionneur = form.cleaned_data['presence_positionneur']
                infoRevisionBIS = form.cleaned_data['infoRevisionBIS']
                
                try : 
                    if num_atelier.id_atelier == 14 and nouveau_atelier:
                        print("Création d'un nouvel atelier")
                        atelier, created = ATELIER.objects.get_or_create(nom_atelier=nouveau_atelier)
                        #atelier.save()
                        atelier = ATELIER.objects.get(nom_atelier=nouveau_atelier)
                    else:
                        # Assumant que num_atelier est une chaîne représentant un ID numérique valide pour un ATELIER existant
                        atelier = num_atelier
            
                except ATELIER.DoesNotExist:
                
                    print("L'atelier n'existe pas")    
                
                if form.cleaned_data['type_vanne'] == '1':
                    type_vannes = 'TOR'
                else:
                    type_vannes = 'REG'
                    
                if type_effet == '1':
                    type_effet = 'SIMPLE'
                else:
                    type_effet = 'DOUBLE'
                
                if type_contact_actionneur == '1':
                    type_contact_actionneur = 'OUVERTURE'
                elif type_contact_actionneur == '2':
                    type_contact_actionneur = 'FERMETURE'
                else:
                    type_contact_actionneur = 'OUVERTURE + FERMETURE'
                    
                
                if sens_actionneur == '1':
                    sens_actionneur = 'OMA'
                elif sens_actionneur == '2':
                    sens_actionneur = 'FMA'
                else:
                    sens_actionneur = 'Aucune de caractéritiques'
                
                if sens_action == '1':
                    sens_action = 'DIRECT'
                else:
                    sens_action = 'INVERSE'
                    
                if infoRevisionBIS == '1':
                    revision = now.replace(year=now.year + tempsRev) if not (now.month == 2 and now.day == 29 and (now.year + tempsRev) % 4 != 0) else now.replace(year=now.year + tempsRev, month=3, day=1)
                    revision = revision.year
                else:
                    revision = None
            
                            
                try : 
                    if num_fournisseur_actionneur.id_fournisseur == 45 and nouveau_fournisseur_actionneur:
                        print("fournisseur actionneur n'existe pas")
                        frn_act, created = FOURNISSEUR.objects.get_or_create(nom_fournisseur=nouveau_fournisseur_actionneur)
                        #atelier.save()
                        frn_act = FOURNISSEUR.objects.get(nom_fournisseur=nouveau_fournisseur_actionneur)
                    else:
                        # Assumant que num_atelier est une chaîne représentant un ID numérique valide pour un ATELIER existant
                        frn_act = num_fournisseur_actionneur
            
                except FOURNISSEUR.DoesNotExist:
                    print("Le fournisseur n'existe pas")
                    
                try : 
                    if num_fournisseur.id_fournisseur == 45 and nouveau_fournisseur:
                        print("fournisseur corps n'existe pas")
                        frn, created = FOURNISSEUR.objects.get_or_create(nom_fournisseur=nouveau_fournisseur)
                        #atelier.save()
                        frn = FOURNISSEUR.objects.get(nom_fournisseur=nouveau_fournisseur)
                    else:
                        # Assumant que num_atelier est une chaîne représentant un ID numérique valide pour un ATELIER existant
                        frn = num_fournisseur
            
                except FOURNISSEUR.DoesNotExist:
                    print("Le fournisseur n'existe pas")
                
                try : 
                    if num_fournisseur_positionneur.id_fournisseur == 45 and nouveau_fournisseur_positionneur:
                        print("fournisseur positionneur n'existe pas")
                        frn_pos, created = FOURNISSEUR.objects.get_or_create(nom_fournisseur=nouveau_fournisseur_positionneur)
                        #atelier.save()
                        frn_pos = FOURNISSEUR.objects.get(nom_fournisseur=nouveau_fournisseur_positionneur)
                    else:
                        # Assumant que num_atelier est une chaîne représentant un ID numérique valide pour un ATELIER existant
                        frn_pos = num_fournisseur_positionneur
            
                except FOURNISSEUR.DoesNotExist:
                    print("Le fournisseur n'existe pas")
                    
                    
            
                # Sauvegarder l'objet Vanne
                
            # Sauvegarder l'objet CORPS d'abord
                corps = CORPS(
                    id_fournisseur=frn,
                    dn_corps=taille_corps, 
                    code_corps=code_corps, 
                    type_corps=type_corps, 
                    pn_corps=pn_corps, 
                    cv_corps=cv_corps, 
                    num_serie_corps=numero_serie_corps, 
                    corps_corps=corps_corps, 
                    norme_bride_corps=norme_bride_corps, 
                    matiere_garnitures_corps=garniture_corps,
                    type_garniture_corps=type_garniture, 
                    matiere_arbre_corps=matiere_arbre, 
                    matiere_siege_corps=matiere_siege, 
                    matiere_org_reglant_corps=matiere_organe_reglant
                )
                # Sauvegardez l'objet CORPS avant de l'assigner à Vanne

                # Ensuite, sauvegarder l'objet ACTIONNEUR
                actionneur = ACTIONNEUR(
                    id_fournisseur=frn_act,
                    type_actionneur=type_actionneur, 
                    num_serie_actionneur=numero_serie_actionneur, 
                    taille_actionneur=taille_actionneur, 
                    type_contact_actionneur=type_contact_actionneur, 
                    pression_alimentation=pression_alimentation, 
                    sens_actionneur=sens_actionneur, 
                    contact_ouv_ferm_actionneur=type_contact, 
                    actionneur_simpl_double_effet=type_effet, 
                    commande_manuel=commande_manuelle_actionneur
                )
                
                pos = POSITIONNEUR(
                    id_fournisseur=frn_pos,
                    fonctionnement_positionneur=id_fonctionnement_positionneur,
                    type_positionneur=type_positionneur, 
                    num_serie_positionneur=numero_serie_positionneur, 
                    signal_sortie=signal_sortie_positionneur, 
                    signal_entre_positionneur=signal_entree_positionneur, 
                    repere_came=repere_came_positionneur, 
                    face_came = face_came_positionneur, 
                    sens_action=sens_action,
                    presion_positionneur=pression_alimentation_positionneur,
                    fermer_a = fermee_a_positionneur,
                    ouvert_a = ouverte_a_positionneur,
                    loi_positionneur = loi_pos
                )

                # Créer l'objet Vanne avec les objets liés déjà sauvegardés
                van = Vanne(
                    id_corps=corps,
                    id_actionneur=actionneur,
                    id_positionneur = pos,
                    freq_revision = tempsRev,
                    voir_en = revision,
                    repere_vanne=request.POST.get('repere_vanne'), 
                    affectation_vanne=request.POST.get('affectation_vanne'),
                    type_vannes=type_vannes, 
                    numero_commande=request.POST.get('numero_commande'),
                    id_atelier=atelier,
                    date_commande= datetime.now()
                )
                
                vanSansPos = Vanne(
                    id_corps=corps,
                    id_actionneur=actionneur,
                    freq_revision = tempsRev,
                    voir_en = revision,
                    repere_vanne=request.POST.get('repere_vanne'), 
                    affectation_vanne=request.POST.get('affectation_vanne'),
                    type_vannes=type_vannes, 
                    numero_commande=request.POST.get('numero_commande'),
                    id_atelier=atelier,
                    date_commande=datetime.now()
                )
                corps.full_clean()
                actionneur.full_clean()
                pos.full_clean()
                
                if save == True:
                    corps.save()
                    actionneur.save() 
                    
                    
                    if presence_positionneur == '1':
                        pos.save()
                        van.save()
                    else:
                        vanSansPos.save()
                    
                    success = True
                else:
                    success = False
                

                
                #return render(request, 'appliVanne/creationVanne.html', {sucess: sucess})
                #form.save()
                #LesVannes  = Vanne.objects.all()
                return render(request, "appliVanne/vannes.html", {"sucess": success, "listeVannes": LesVannes})
            else:
                # Le formulaire n'est pas valide, renvoyez le formulaire avec les erreurs
                return render(request, 'appliVanne/creationVanne.html', {
                    'form': form, "listVannes": LesVannes, "listAtelier": LesAtelier,
                    "listFournisseur": lesFournisseur, "listTypePos": typePos
                })
        else:
            # Si la requête n'est pas un POST, initialisez un formulaire vide et renvoyez-le
            form = VanneForm()
            return render(request, 'appliVanne/creationVanne.html', {
                'form': form, "listVannes": LesVannes, "listAtelier": LesAtelier,
                "listFournisseur": lesFournisseur, "listTypePos": typePos
            })
            # Si la requête n'est pas un POST, affichez simplement le formulaire vide
    else:
        return redirect('login')
    
def edit(request, id_vanne):
    if request.user.is_authenticated:

        LesVannes  = Vanne.objects.all()
        LesAtelier  = ATELIER.objects.all()
        lesFournisseur = FOURNISSEUR.objects.all() 
        typePos = TYPEPOSITIONNEUR.objects.all()
        
        lavanne = Vanne.objects.get(id_vanne=id_vanne)
        return render(request, "appliVanne/edit.html", {"vanne": lavanne, "listVannes": LesVannes, "listAtelier": LesAtelier, "listFournisseur": lesFournisseur, "listTypePos": typePos})
    else:
        return redirect('login')
    
def traitementModifVanne(request):
    if request.user.is_authenticated:

        if request.method == "POST":
            id_vanne_form = request.POST.get('id_vanne')
            vanne = get_object_or_404(Vanne, id_vanne=id_vanne_form)  # Utilise get_object_or_404 pour simplifier
            form = VanneForm(request.POST, instance=vanne)
            now = datetime.now()
            
            

            if form.is_valid():
                
                # Mettre à jour l'objet Vanne directement
                vanne.repere_vanne = form.cleaned_data['repere_vanne']
                vanne.affectation_vanne = form.cleaned_data['affectation_vanne']
                vanne.numero_commande = form.cleaned_data['numero_commande']
                vanne.date_commande = form.cleaned_data['date_de_la_commande']
                # Ajoutez ici toute autre logique spécifique pour la mise à jour des champs de l'objet Vanne


                # Mettre à jour l'objet Corps associé à la vanne
                corps = vanne.id_corps
                corps.dn_corps = form.cleaned_data['taille_corps']
                corps.code_corps = form.cleaned_data['code_corps']
                corps.type_corps = form.cleaned_data['type_corps']
                corps.pn_corps = form.cleaned_data['pn_corps']
                corps.cv_corps = form.cleaned_data['cv_corps']
                corps.num_serie_corps = form.cleaned_data['numero_serie_corps']
                corps.corps_corps = form.cleaned_data['corps_corps']
                corps.norme_bride_corps = form.cleaned_data['norme_bride_corps']
                corps.matiere_garnitures_corps = form.cleaned_data['garniture_corps']
                corps.type_garniture_corps = form.cleaned_data['type_garniture']
                corps.matiere_arbre_corps = form.cleaned_data['matiere_arbre']
                corps.matiere_siege_corps = form.cleaned_data['matiere_siege']
                corps.matiere_org_reglant_corps = form.cleaned_data['matiere_organe_reglant']
                # Ajoutez ici toute autre logique spécifique pour la mise à jour des champs de l'objet Corps


                # Mettre à jour l'objet Actionneur associé à la vanne
                actionneur = vanne.id_actionneur
                actionneur.taille_actionneur = form.cleaned_data['taille_actionneur']
                actionneur.type_actionneur = form.cleaned_data['type_actionneur']
                actionneur.num_serie_actionneur = form.cleaned_data['numero_serie_actionneur']
                actionneur.commande_manuel = form.cleaned_data['commande_manuelle_actionneur']
                actionneur.sens_actionneur = form.cleaned_data['sens_actionneur']
                actionneur.pression_alimentation = form.cleaned_data['pression_alimentation']
                actionneur.type_contact_actionneur = form.cleaned_data['type_contact']
                actionneur.type_contact_actionneur = form.cleaned_data['type_contact_actionneur']
                # Ajoutez ici toute autre logique spécifique pour la mise à jour des champs de l'objet Actionneur

                
                num_atelier = form.cleaned_data['id_atelier']
                nouveau_atelier = form.cleaned_data['nouveau_atelier']
                
                vanne.id_actionneur.id_fournisseur = choixFournisseur(form.cleaned_data['id_fournisseur_actionneur'], form.cleaned_data['nouveau_fournisseur_actionneur'])
                vanne.id_corps.id_fournisseur = choixFournisseur(form.cleaned_data['id_fournisseur'], form.cleaned_data['nouveau_fournisseur'])
                try : 
                    if num_atelier.id_atelier == 14 and nouveau_atelier:
                        print("Création d'un nouvel atelier")
                        atelier, created = ATELIER.objects.get_or_create(nom_atelier=nouveau_atelier)
                        #atelier.save()
                        atelier = ATELIER.objects.get(nom_atelier=nouveau_atelier)
                    else:
                        # Assumant que num_atelier est une chaîne représentant un ID numérique valide pour un ATELIER existant
                        atelier = num_atelier
                        
                    if atelier != 13 or atelier != 14:
                        vanne.en_service_vanne = 1
                    if atelier == 13:
                        vanne.en_service_vanne = 2
                    if atelier == 14:
                        vanne.en_service_vanne = 3
                    
            
                except ATELIER.DoesNotExist:
                    print("erreur")
                
                vanne.id_atelier = atelier
                
                infoRevisionBIS = form.cleaned_data['infoRevisionBIS']
                tempsRev = form.cleaned_data['tempsRev']
                
                if vanne.derniere_revision == None and vanne.voir_en != None:
                    vanne.derniere_revision = vanne.voir_en - vanne.freq_revision
                
                if infoRevisionBIS == '1':
                    if (vanne.voir_en != None):
                        revision = vanne.derniere_revision + tempsRev
                    else:
                        revision = now.replace(year=now.year + tempsRev) if not (now.month == 2 and now.day == 29 and (now.year + tempsRev) % 4 != 0) else now.replace(year=now.year + tempsRev, month=3, day=1)
                        revision = revision.year
                else:
                    revision = None
                    
                vanne.voir_en = revision
                vanne.freq_revision = tempsRev
                    
                commande_manuelle_actionneur = form.cleaned_data['commande_manuelle_actionneur']
                sens_actionneur = form.cleaned_data['sens_actionneur']
                type_effet = form.cleaned_data['type_effet']
                type_contact_actionneur = form.cleaned_data['type_contact_actionneur']
                
                if form.cleaned_data['type_vanne'] == '1':
                    vanne.type_vannes = 'TOR'
                else:
                    vanne.type_vannes = 'REG'
                    
                if type_effet == '1':
                    vanne.id_actionneur.actionneur_simpl_double_effet = 'SIMPLE'
                else:
                    vanne.id_actionneur.actionneur_simpl_double_effet = 'DOUBLE'
                
                if type_contact_actionneur == '1':
                    vanne.id_actionneur.contact_ouv_ferm_actionneur = 'OUVERTURE'
                elif type_contact_actionneur == '2':
                    vanne.id_actionneur.contact_ouv_ferm_actionneur = 'FERMETURE'
                elif type_contact_actionneur == '3':
                    vanne.id_actionneur.contact_ouv_ferm_actionneur = 'OUVERTURE + FERMETURE'
                else:
                    vanne.id_actionneur.contact_ouv_ferm_actionneur = 'NC'  
                
                if sens_actionneur == '1':
                    vanne.id_actionneur.sens_actionneur = 'OMA'
                elif sens_actionneur == '2':
                    vanne.id_actionneur.sens_actionneur = 'FMA'
                else:
                    vanne.id_actionneur.sens_actionneur = 'Aucune de caractéritiques'
                

                # Extraction des données du formulaire déjà validé
                num_fournisseur_positionneur = form.cleaned_data['id_fournisseur_positionneur']
                nouveau_fournisseur_positionneur = form.cleaned_data['nouveau_fournisseur_positionneur']
                presence_positionneur = request.POST.get('presence_positionneur')
                
                # Gestion du fournisseur positionneur
                if num_fournisseur_positionneur.id_fournisseur == 45 and nouveau_fournisseur_positionneur:
                    frn_pos, created = FOURNISSEUR.objects.get_or_create(nom_fournisseur=nouveau_fournisseur_positionneur)
                else:
                    frn_pos = num_fournisseur_positionneur

                # Mise à jour ou création du positionneur selon la présence
                if presence_positionneur == '1':
                    if form.cleaned_data['sens_action'] == '1':
                        sensPos = 'DIRECT'
                    else:
                        sensPos = 'INVERSE'
                        
                    input_value = form.cleaned_data['ouverte_a_positionneur']

# Utilise re.findall pour extraire tous les nombres de la chaîne
                    numbers = re.findall(r'\d+', input_value)

                    # Si vous vous attendez à un seul nombre, prenez le premier élément et convertissez-le en entier
                    if numbers:
                        ouvert_a_value = int(numbers[0])
                    else:
                        ouvert_a_value = 0 
                    positionneur_data = {
                        'id_fournisseur': frn_pos,
                        'fonctionnement_positionneur': form.cleaned_data['id_fonctionnement_positionneur'],
                        'type_positionneur': form.cleaned_data['type_positionneur'],
                        'num_serie_positionneur': form.cleaned_data['numero_serie_positionneur'],
                        'signal_sortie': form.cleaned_data['signal_sortie_positionneur'],
                        'signal_entre_positionneur': form.cleaned_data['signal_entree_positionneur'],
                        'repere_came': form.cleaned_data['repere_came_positionneur'],
                        'face_came': form.cleaned_data['face_came_positionneur'],
                        'sens_action': sensPos,
                        'presion_positionneur': form.cleaned_data['alimentation_positionneur'],
                        'fermer_a': form.cleaned_data['fermee_a_positionneur'],
                        'ouvert_a': ouvert_a_value,
                        'loi_positionneur': form.cleaned_data['loi_commande_positionneur'],
                    }
                    if vanne.id_positionneur:
                        for key, value in positionneur_data.items():
                            setattr(vanne.id_positionneur, key, value)
                        vanne.id_positionneur.save()
                    else:
                        positionneur = POSITIONNEUR(**positionneur_data)
                        positionneur.save()
                        vanne.id_positionneur = positionneur
                else:
                    vanne.id_positionneur = None # Enlève le positionneur si non présent


                user = User.objects.get(username=request.user)
            
                 # Créez une révision pour la vanne
                create_revision_for_changes(vanne, "l'information général", user, vanne.id_vanne)
                create_revision_for_changes(corps, "Corps", user, vanne.id_vanne)
                create_revision_for_changes(actionneur, "Actionneur", user, vanne.id_vanne)

                # Créez une révision pour le positionneur
                if vanne.id_positionneur is not None:
                    create_revision_for_changes(vanne.id_positionneur, "Positionneur", user, vanne.id_vanne)



                
               

                vanne.full_clean()
                vanne.id_corps.full_clean()
                vanne.id_actionneur.full_clean()



                vanne.id_actionneur.save()
                vanne.id_corps.save()
                vanne.save()
                

                
                return redirect('detail_vanne', id_vanne=id_vanne_form)
            else:
                print(form.errors)
                # Le formulaire n'est pas valide, afficher à nouveau avec erreurs
                context = {
                    'form': form,
                    "listVannes": Vanne.objects.all(),
                    "listAtelier": ATELIER.objects.all(),
                    "listFournisseur": FOURNISSEUR.objects.all(),
                    "listTypePos": TYPEPOSITIONNEUR.objects.all()
                }
                return render(request, 'appliVanne/creationVanne.html', context)
        else:
            # Si pas POST, rediriger vers la page de modification/ajout
            return redirect('url_vers_page_modification_ou_ajout')
    else:
        return redirect('login')


def create_revision_for_changes(obj, type_name, user,id_vanne):
    has_changes = any(obj.tracker.has_changed(field) for field in obj.tracker.fields)
    if has_changes:
        detail_commentaire = "</br> ".join(
            f"{obj._meta.get_field(field).verbose_name} a changé de <strong> {obj.tracker.previous(field)} </strong> à <strong>{getattr(obj, field)} </strong>"
            for field in obj.tracker.fields
            if obj.tracker.has_changed(field)
        )
        REVISON(
            rev_id_vanne= id_vanne,  # Ou une autre manière de référencer votre vanne
            date_revision=datetime.now(),
            type_revision="Modification ",
            commentaire_revision=f"Modification de {type_name.lower()}",
            detail_commentaire=detail_commentaire,
            nom_technicien=f"{user.first_name} {user.last_name}"
        ).save()
        
def supressionTOTAL (request, id_vanne):
    if request.user.is_authenticated:
        vanne = get_object_or_404(Vanne, id_vanne=id_vanne)
        
        rev = REVISON(
            rev_id_vanne= id_vanne,
            date_revision=datetime.now(),
            id_revision_vanne = numRev(id_vanne),
            type_revision = "Suppression",
            commentaire_revision="Suppression TOTAL de la vanne, pas d'historique disponible",
            nom_technicien = request.user.first_name + " " + request.user.last_name

        )
        rev.full_clean()
        rev.save()
        
        
        if vanne.id_positionneur != None:
            vanne.id_actionneur.delete()
        if vanne.id_corps != None:
            vanne.id_corps.delete()
        if vanne.id_positionneur != None:
            vanne.id_positionneur.delete()
        vanne.delete()
        
    
        
        return redirect('vannes')
    else:
        return redirect('login')
    
def choixFournisseur(num_fournisseur, nouveau_fournisseur):

    try : 
        if num_fournisseur.id_fournisseur == 45 and nouveau_fournisseur:
            print("fournisseur actionneur n'existe pas")
            frn_act, created = FOURNISSEUR.objects.get_or_create(nom_fournisseur=nouveau_fournisseur)
            #atelier.save()
            frn_act = FOURNISSEUR.objects.get(nom_fournisseur=nouveau_fournisseur)
        else:
            # Assumant que num_atelier est une chaîne représentant un ID numérique valide pour un ATELIER existant
            frn_act = num_fournisseur
    
    except FOURNISSEUR.DoesNotExist:
        frn_act = "Le fournisseur n'existe pas"
        print("Le fournisseur n'existe pas")
    return frn_act

def revision(request, id_vanne):
    if request.user.is_authenticated:
        form = CommentForm()
        vanne = get_object_or_404(Vanne, id_vanne=id_vanne)
        infoRev = REVISON.objects.filter(rev_id_vanne=id_vanne)
        lesRev = REVISON.objects.all().count()
        
        return render(request, "appliVanne/revision.html", {"vanne": vanne, "infoRevision":infoRev, "form": form, "lesRev": lesRev})
    else:
        return redirect('login')
    
def TraitementRevision(request, id_vanne):
    if request.user.is_authenticated:
        
        vanne = get_object_or_404(Vanne, id_vanne=id_vanne)
        now = datetime.now()
        tempsRev = vanne.freq_revision
        revision = now.replace(year=now.year + tempsRev) if not (now.month == 2 and now.day == 29 and (now.year + tempsRev) % 4 != 0) else now.replace(year=now.year + tempsRev, month=3, day=1)
        vanne.voir_en = revision.year
        vanne.derniere_revision = now.year
        vanne.save()



        rev = REVISON(
            ajout_revision = "MANU",
            rev_id_vanne=id_vanne,
            date_revision=now,
            id_revision_vanne = numRev(id_vanne),
            type_revision = "Révision",
            commentaire_revision="Révion effectuée",
            detail_commentaire = request.POST.get('commentaire'),
            nom_technicien = request.user.first_name + " " + request.user.last_name
        )
        rev.full_clean()
        rev.save()
        return redirect('detail_vanne', id_vanne=id_vanne)
    else:
        return redirect('login')

def detail_revision(request, id_revision):
    if request.user.is_authenticated:

        infoRev = get_object_or_404(REVISON,id_revision=id_revision)
        return render(request, "appliVanne/detailRevision.html", { "infoRevision":infoRev })
    else:
        return redirect('login')
       
def printer(request, id_vanne):
    vanne = Vanne.objects.get(id_vanne=id_vanne)
    infoRev = REVISON.objects.filter(rev_id_vanne=id_vanne)
    return render(request, "appliVanne/print.html", {"vanne": vanne, "infoRevision":infoRev })

def numRev(id_vanne):
    
    infoRev = REVISON.objects.filter(rev_id_vanne=id_vanne).last()
    
    if infoRev == None:
        numREV = 1
    else:
        numREV = infoRev.id_revision_vanne + 1
        
    return numREV

def commente(request, id_vanne):
    CommentFormSet = formset_factory(CommentForm, extra=1)
    if request.method == 'POST':
        formset = CommentFormSet(request.POST)
        if formset.is_valid():
            # Traitez les commentaires validés
            for form in formset:
                form.save()
            # Redirigez ou affichez un message de succès
    else:
        formset = CommentFormSet()
    return render(request, 'appliVanne/commente.html', {'formset': formset})

def handler404(request, exception):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)

def add_commentaire(request, id_vanne):
    if request.user.is_authenticated:
        vanne = get_object_or_404(Vanne, id_vanne=id_vanne)
        infoRev = REVISON.objects.filter(rev_id_vanne=id_vanne)
        lesRev = REVISON.objects.all().count()
        return render(request, "appliVanne/comentaire.html", {"vanne": vanne, "infoRevision":infoRev, "lesRev": lesRev})
    else:
        return redirect('login')