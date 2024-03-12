from django import forms
from django.forms import ModelForm
from appliVanne.models import *
from django.core.exceptions import ValidationError
from django.utils import timezone

import datetime


class VanneForm(ModelForm):
    #information general à la vannes
    
    id_vanne = forms.IntegerField(label="ID Vanne", required=False)
    nouveau_atelier = forms.CharField(label="Information générales : Nouvel Atelier", required=False)
    id_atelier = forms.ModelChoiceField(queryset=ATELIER.objects.all(), empty_label="Information générales : Sélectionnez un atelier", required=False)
    type_vanne = forms.ChoiceField(choices=(('1', 'TOR'), ('2', 'REG')), label="Type de vanne", required=False)
    tempsRev = forms.IntegerField(label="Temps de révision", required=False, error_messages={'required': 'Ce champ est obligatoire.'})
    date_de_la_commande = forms.DateField(label="Information générales : Date de la commande", required=False)
    
    
    
    #CORPS
    nouveau_atelier = forms.CharField(label="Corps : Nouvel Atelier", required=False)
    id_fournisseur = forms.ModelChoiceField(queryset=FOURNISSEUR.objects.all(),empty_label="Corps : Sélectionnez un fournisseur",required=False,label="fournisseur")
    nouveau_fournisseur = forms.CharField(label="Corps : Nom du Nouveau Fournisseur",required=False)  # Rendre ce champ optionnel)
    taille_corps = forms.IntegerField(label="Corps : Taille du corps",required=False)
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
    taille_actionneur = forms.IntegerField(label="Actionneur : Taille de l'actionneur",required=False)
    type_actionneur = forms.CharField(label="Actionneur : Type d'actionneur",required=False)
    numero_serie_actionneur = forms.CharField(label="Actionneur : Numéro de serie" ,required=False)
    commande_manuelle_actionneur = forms.ChoiceField(choices=[(1, 'OUI'), (2, 'NON')])
    sens_actionneur = forms.ChoiceField(choices=[(1, 'OMA'), (2, 'FMA'), (3, 'Aucune de caractéritiques')])
    pression_alimentation = forms.CharField(label="Actionneur : Pression Alim." ,required=False)
    type_contact = forms.CharField(label="Actionneur : Type Contact" ,required=False)
    type_effet = forms.ChoiceField(choices=[(1, 'SIMPLE'), (2, 'DOUBLE')])
    type_contact_actionneur = forms.ChoiceField(choices=[(1, 'OUVERTURE'), (2, 'FERMETURE'), (3, 'OUVERTURE + FERMETURE'),(4, 'NC')])

    #POSITIONNEUR
    presence_positionneur = forms.ChoiceField(choices=[(0, 'NON'), (1, 'OUI')])
    id_fournisseur_positionneur = forms.ModelChoiceField(queryset=FOURNISSEUR.objects.all(),empty_label="Sélectionnez un fournisseur",required=False,label="fournisseur")
    nouveau_fournisseur_positionneur = forms.CharField(label="Nom du Nouveau Fournisseur",required=False)  # Rendre ce champ optionnel)
    id_fonctionnement_positionneur = forms.ModelChoiceField(queryset=TYPEPOSITIONNEUR.objects.all(),required=False,label="fournisseur")
    type_positionneur = forms.CharField(label="Positionneur : Type de positionneur", required=False)
    numero_serie_positionneur = forms.CharField(label="Positionneur : Numéro de serie" , required=False)
    signal_sortie_positionneur = forms.IntegerField(label="Positionneur : Signal de sortie" , required=False)
    signal_entree_positionneur = forms.IntegerField(label="Positionneur : Signal d'entrée" , required=False)
    repere_came_positionneur = forms.IntegerField(label="Positionneur : Repère de la came" , required=False)
    face_came_positionneur = forms.IntegerField(label="Positionneur : Face de la came" , required=False)
    sens_action = forms.ChoiceField(choices=[(1, 'DIRECT'), (2, 'INVERSE')])
    fermee_a_positionneur = forms.IntegerField(label="Positionneur : Fermée à", required=False )
    ouverte_a_positionneur = forms.IntegerField(label="Positionneur : Ouverte à" , required=False)
    alimentation_positionneur = forms.CharField(label="Positionneur : Alimentation" , required=False)
    loi_commande_positionneur = forms.CharField(label="Loi" , required=False )
    
    infoRevisionBIS = forms.ChoiceField(choices=[(0, 'NON'), (1, 'OUI')])
   
    
    class Meta:
        model = Vanne
        fields = ['repere_vanne', 'affectation_vanne', 'numero_commande']
        widgets = {
            'repere_vanne': forms.TextInput(attrs={'required': 'required'}),
            'affectation_vanne': forms.TextInput(attrs={'required': 'required'}),
            'numero_commande': forms.TextInput(attrs={'required': 'required'}),
        }

    
    def clean(self):
        cleaned_data = super().clean()
        num_atelier = cleaned_data.get("id_atelier")  # Assurez-vous que cela correspond au nom du champ dans votre modèle/formulaire
        nouveau_atelier = cleaned_data.get("nouveau_atelier")

        if num_atelier == -1 and not nouveau_atelier:
            raise ValidationError("Veuillez fournir le nom du nouvel atelier.")

        # Vous pouvez ajouter d'autres validations ici si nécessaire


        for field_name, value in cleaned_data.items():
            # Vérifie si la valeur est une chaîne vide pour n'importe quel champ
            if isinstance(value, str) and value.strip() == '':
                cleaned_data[field_name] = None
            # Ajoutez ici toute autre condition spécifique pour d'autres types de champs si nécessaire
            
        date_commande = cleaned_data.get("date_de_la_commande")
        if not date_commande:
            cleaned_data['date_de_la_commande'] = timezone.now().date()
        
        return cleaned_data
    
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = REVISON
        fields = ['commentaire_revision']