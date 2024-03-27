
from django.test import TestCase
from django.urls import reverse
from django.test import Client
from appliVanne.models import MaModel
from applicompte.models import AutreModel
from appliVanne.forms import MonFormulaire

# Tests de modèles
class ModelTests(TestCase):

    def test_model_ma_model(self):
        # Créer une instance de MaModel
        instance = MaModel(attribut='valeur')
        instance.save()
        
        # Vérifier si l'instance est bien sauvegardée
        self.assertEqual(MaModel.objects.count(), 1)
        self.assertEqual(MaModel.objects.first(), instance)

    def test_model_autre_model(self):
        # Test similaire pour AutreModel
        pass

# Tests de vues
class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_une_vue(self):
        response = self.client.get(reverse('nom_de_la_vue'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'nom_du_template.html')

# Tests de formulaires
class FormTests(TestCase):

    def test_mon_formulaire_valide(self):
        form_data = {'champ1': 'valeur1', 'champ2': 'valeur2'}
        form = MonFormulaire(data=form_data)
        self.assertTrue(form.is_valid())

    def test_mon_formulaire_invalide(self):
        form_data = {'champ1': 'valeur incorrecte'}
        form = MonFormulaire(data=form_data)
        self.assertFalse(form.is_valid())
