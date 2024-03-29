from django import forms
from django.forms import ModelForm
from appliVanne.models import *
from django.core.exceptions import ValidationError
from django.utils import timezone
from tinymce.widgets import TinyMCE
import datetime


class VanneForm(ModelForm):
    #information general à la vannes
    
    id_vanne = forms.IntegerField(label="ID Vanne", required=False)
    nouveau_atelier = forms.CharField(label="Information générales : Nouvel Atelier", required=False)
    id_atelier = forms.ModelChoiceField(queryset=ATELIER.objects.all(), empty_label="Information générales : Sélectionnez un atelier", required=False)
    id_fournisseur = forms.ModelChoiceField(queryset=FOURNISSEUR.objects.all(),empty_label="Corps : Sélectionnez un fournisseur",required=False,label="fournisseur")

    type_vanne = forms.ChoiceField(choices=(('TOR', 'TOR'), ('REG', 'REG')), label="Type de vanne", required=True)
    tempsRev = forms.IntegerField(label="Temps de révision", required=False, error_messages={'required': 'Ce champ est obligatoire.'})
    date_de_la_commande = forms.DateField(label="Information générales : Date de la commande", required=False)
    
    
    
    #CORPS
    nouveau_atelier = forms.CharField(label="Corps : Nouvel Atelier", required=False)
    nouveau_fournisseur = forms.CharField(label="Corps : Nom du Nouveau Fournisseur",required=False)  # Rendre ce champ optionnel)
    taille_corps = forms.CharField(label="Corps : Taille du corps",required=False)
    code_corps = forms.CharField(label="Corps : Code du corps",required=False) 
    type_corps = forms.CharField(label="Corps : Type de corps",required=False)
    pn_corps = forms.CharField(label="Corps : PN Corps", required=False)
    cv_corps = forms.CharField(label="Corps : CV Corps", required=False)
    numero_serie_corps = forms.CharField(label="Corps : Numéro de série corps", required=False)
    corps_corps = forms.CharField(label="Corps : Matière du corps", required=False)
    norme_bride_corps = forms.CharField(label="Corps : Norme bride corps", required=False)
    garniture_corps = forms.CharField(label="Corps : Garniture corps", required=False)
    type_garniture = forms.CharField(label="Corps : Type Ganiture corps", required=False)    
    matiere_arbre = forms.CharField(label="Corps : Matière arbre", required=False)
    matiere_siege = forms.CharField(label="Corps : Matière siège", required=False)
    matiere_organe_reglant = forms.CharField(label="Corps : Matière organe réglant", required=False)

    #ACTIONNEUR
    id_fournisseur_actionneur = forms.ModelChoiceField(queryset=FOURNISSEUR.objects.all(),empty_label="Actionneur : Sélectionnez un fournisseur",required=False,label="fournisseur")
    nouveau_fournisseur_actionneur = forms.CharField(label="Actionneur : Nom du Nouveau Fournisseur",required=False)  # Rendre ce champ optionnel)
    taille_actionneur = forms.CharField(label="Actionneur : Taille de l'actionneur",required=False)
    type_actionneur = forms.CharField(label="Actionneur : Type d'actionneur",required=False)
    numero_serie_actionneur = forms.CharField(label="Actionneur : Numéro de serie" ,required=False)
    commande_manuelle_actionneur = forms.ChoiceField(choices=[('OUI', 'OUI'), ('NON', 'NON') ], required=False)
    sens_actionneur = forms.ChoiceField(choices=[('OMA', 'OMA'), ('FMA', 'FMA')],required=False)
    pression_alimentation = forms.CharField(label="Actionneur : Pression Alim." ,required=False)
    type_contact = forms.CharField(label="Actionneur : Type Contact" ,required=False)
    type_effet = forms.ChoiceField(choices=[('SIMPLE', 'SIMPLE'), ('DOUBLE', 'DOUBLE')],required=False)
    type_contact_actionneur = forms.ChoiceField(choices=[('OUVERTURE', 'OUVERTURE'), ('FERMETURE', 'FERMETURE'), ('FERM+OUVER', 'OUVERTURE + FERMETURE')],required=False)

    #POSITIONNEUR
    presence_positionneur = forms.ChoiceField(choices=[(0, 'NON'), (1, 'OUI')])
    id_fournisseur_positionneur = forms.ModelChoiceField(queryset=FOURNISSEUR.objects.all(),empty_label="Sélectionnez un fournisseur",required=False,label="fournisseur")
    nouveau_fournisseur_positionneur = forms.CharField(label="Nom du Nouveau Fournisseur",required=False)  # Rendre ce champ optionnel)
    id_fonctionnement_positionneur = forms.ModelChoiceField(queryset=TYPEPOSITIONNEUR.objects.all(),required=False,label="fonctionnement")
    type_positionneur = forms.CharField(label="Positionneur : Type de positionneur", required=False)
    numero_serie_positionneur = forms.CharField(label="Positionneur : Numéro de serie" , required=False)
    signal_sortie_positionneur = forms.CharField(label="Positionneur : Signal de sortie" , required=False)
    signal_entree_positionneur = forms.CharField(label="Positionneur : Signal d'entrée" , required=False)
    repere_came_positionneur = forms.CharField(label="Positionneur : Repère de la came" , required=False)
    face_came_positionneur = forms.CharField(label="Positionneur : Face de la came" , required=False)
    sens_action = forms.ChoiceField(choices=[('DIRECT', 'DIRECT'), ('INVERSE', 'INVERSE')],required=False)
    fermee_a_positionneur = forms.CharField(label="Positionneur : Fermée à", required=False )
    ouverte_a_positionneur = forms.CharField(label="Positionneur : Ouverte à" , required=False)
    alimentation_positionneur = forms.CharField(label="Positionneur : Alimentation" , required=False)
    loi_commande_positionneur = forms.CharField(label="Loi" , required=False )
    
    infoRevisionBIS = forms.ChoiceField(choices=[(0, 'NON'), (1, 'OUI')])#a revoir
    repere_vanne = forms.CharField(label="Repère de la vanne", required=True)
    affectation_vanne = forms.CharField(label="Affectation de la vanne", required=True)
    numero_commande = forms.CharField(label="Numéro de la commande", required=False)
    
    class Meta:
        model = Vanne
        fields = ['repere_vanne', 'affectation_vanne', 'numero_commande']
      
    
    def clean(self):
        cleaned_data = super().clean()
        num_atelier = cleaned_data.get("id_atelier")  # Assurez-vous que cela correspond au nom du champ dans votre modèle/formulaire
        nouveau_atelier = cleaned_data.get("nouveau_atelier")

        if num_atelier == -1 and not nouveau_atelier:
            raise ValidationError("Veuillez fournir le nom du nouvel atelier.")

        # Vous pouvez ajouter d'autres validations ici si nécessaire


        # Liste des champs à exclure
        champs_exclus = [
            'affectation_vanne', 'sens_action', 'infoRevisionBIS', 
            'presence_positionneur', 'type_contact_actionneur', 'type_effet',
            'sens_actionneur', 'commande_manuelle_actionneur', 'type_vanne'
        ]

        for field_name, value in cleaned_data.items():
            # S'assure que le champ n'est pas dans la liste des exclus et que la valeur n'est pas None
            if field_name not in champs_exclus and value is not None and isinstance(value, str):
                # Supprime tous les espaces
                value = value.replace(" ", "")
                # Remplace les virgules par des points
                value = value.replace(",", ".")
                # Convertit tout en majuscules
                value = value.upper()

                # Après transformation, vérifie si la valeur est une chaîne vide ou 'NONE'
                if value == '' or value == 'NONE':  # Pas besoin de strip ici car il n'y a pas d'espace
                    cleaned_data[field_name] = None
                else:
                    cleaned_data[field_name] = value
            # Si le champ est dans les exclus ou la valeur est None, il n'est pas modifié
            # Ajoutez ici toute autre condition spécifique pour d'autres types de champs si nécessaire

                
        date_commande = cleaned_data.get("date_de_la_commande")
        print ("test date commande")
        print(date_commande)
        print ("fin test date commande")

        
        if not date_commande:
            print ("TEST 2 date commande")
            print (self.cleaned_data['date_de_la_commande'])
            self.cleaned_data['date_de_la_commande'] = timezone.now().date()
            print ("TEST 2 FIN date commande")

        return cleaned_data

        
    
class CommentForm(forms.ModelForm):
    
    commentaire = forms.CharField(label="Revision" , required=True,  widget=TinyMCE(attrs={'cols': 80, 'rows': 30}) )

    class Meta:
        model = REVISON
        fields = ['commentaire']
        
        
class ajoutDeCom(forms.ModelForm):
    detail_commentaire = forms.CharField(label="Commentaire", required=False, widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    id_type_revision = forms.ModelChoiceField(queryset=TypeRevision.objects.all(), empty_label="Sélectionnez un type de commentaire", required=False, label="Type de commentaire")
    nouveau_type_commentaire = forms.CharField(label="Nouveau type de commentaire", required=False)
    object_commentaire = forms.CharField(label="Objet", required=True)
    
    class Meta:
        model = REVISON
        fields = ['detail_commentaire', 'object_commentaire']
        
    def clean(self):
        cleaned_data = super().clean()
        id_type_revision = cleaned_data.get("id_type_revision")        

class FusionFournisseurForm(forms.Form):
    fournisseurs_a_fusionner = forms.ModelMultipleChoiceField(queryset=FOURNISSEUR.objects.all(), widget=forms.CheckboxSelectMultiple)
    nouveau_nom = forms.CharField(max_length=100)
    
    
class renomerFournisseurForm(forms.Form):
        fournisseurs_a_renomer = forms.ModelChoiceField(queryset=FOURNISSEUR.objects.all(),required=True,label="Fournisseur à renommer")
        nouveau_nom = forms.CharField(max_length=100, label="Nouveau nom du fournisseur")
