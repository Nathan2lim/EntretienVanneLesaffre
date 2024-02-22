from django import forms
from django.forms import ModelForm
from appliVanne.models import *
from django.core.exceptions import ValidationError


class VanneForm(ModelForm):
    nouveau_atelier = forms.CharField(label="Nouvel Atelier", required=False)
    id_atelier = forms.ModelChoiceField(queryset=ATELIER.objects.all(), empty_label="Sélectionnez un atelier", required=False)
    type_vanne = forms.ChoiceField(choices=(('1', 'TOR'), ('2', 'REG')), label="Type de vanne", required=True)
    nouveau_atelier = forms.CharField(label="Nouvel Atelier", required=False)

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

        return cleaned_data