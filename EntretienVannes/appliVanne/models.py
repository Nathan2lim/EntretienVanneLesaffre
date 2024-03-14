# SQLEditor export: Python Django Model
from django.db import models
import datetime
from django.utils import formats
from applicompte.models import *
from model_utils import FieldTracker


class ATELIER(models.Model):
    class Meta:
        db_table = 'ATELIER'
         
    id_atelier = models.AutoField(primary_key=True, unique=True)
    nom_atelier = models.CharField(max_length=45, default='a remplir', unique=True)

  
class FOURNISSEUR(models.Model): 
    class Meta:
        db_table = 'FOURNISSEUR'
        
    id_fournisseur = models.AutoField(primary_key=True, unique=True)
    nom_fournisseur = models.CharField(max_length=255)
    email_fournisseur = models.EmailField()
    tel_fournisseur = models.CharField(max_length=255)

  
class ACTIONNEUR(models.Model):
    
    class Meta:
        db_table = 'ACTIONNEUR'
        
    id_actionneur = models.AutoField(primary_key=True, unique=True)
    id_fournisseur = models.ForeignKey('FOURNISSEUR', to_field='id_fournisseur', on_delete=models.CASCADE)
    num_serie_actionneur = models.CharField(max_length=255, null=True, blank=True)
    type_actionneur = models.CharField(max_length=255, null=True, blank=True)
    taille_actionneur = models.CharField(max_length=255, null=True, blank=True)
    type_contact_actionneur = models.CharField(max_length=255, null=True, blank=True)
    pression_alimentation = models.CharField(max_length=255, null=True, blank=True)
    sens_actionneur = models.CharField(max_length=255, null=True, blank=True)
    contact_ouv_ferm_actionneur = models.CharField(max_length=255, null=True, blank=True)
    actionneur_simpl_double_effet = models.CharField(max_length=255, null=True, blank=True)
    commande_manuel = models.CharField(max_length=255, null=True, blank=True)
    tracker = FieldTracker()
  
class CORPS(models.Model): 
    class Meta:
        db_table = 'CORPS'
        
    id_corps = models.AutoField(primary_key=True, unique=True, )
    id_fournisseur = models.ForeignKey('FOURNISSEUR', to_field='id_fournisseur', on_delete=models.CASCADE)
    type_corps = models.CharField(max_length=255,null=True, blank=True)
    num_serie_corps = models.CharField(max_length=255,null=True, blank=True)
    dn_corps = models.CharField(max_length=255,null=True, blank=True)
    pn_corps = models.CharField(max_length=255,null=True, blank=True)
    cv_corps = models.CharField(max_length=255,null=True, blank=True)
    norme_bride_corps = models.CharField(max_length=255,null=True, blank=True)
    code_corps = models.CharField(max_length=255,null=True, blank=True)
    matiere_arbre_corps = models.CharField(max_length=255,null=True, blank=True)
    matiere_siege_corps = models.CharField(max_length=255,null=True, blank=True)
    matiere_org_reglant_corps = models.CharField(max_length=255,null=True, blank=True)
    corps_corps = models.CharField(max_length=255,null=True, blank=True)
    matiere_garnitures_corps = models.CharField(max_length=255,null=True, blank=True)
    type_garniture_corps = models.CharField(max_length=255,null=True, blank=True)
    tracker = FieldTracker()
  
class TYPEPOSITIONNEUR(models.Model): 
    
    class Meta:
        db_table = 'TYPEPOSITIONNEUR'
        
    id_fonctionnement_postionneur = models.AutoField(primary_key=True, unique=True)
    description_type_positionneur = models.CharField(max_length=255, blank=True)
    type_positionneur = models.CharField(max_length=255, blank=True)
  
class POSITIONNEUR(models.Model): 
    
    class Meta:
        db_table = 'POSITIONNEUR'
        
    id_positionneur = models.AutoField(primary_key=True, unique=True)
    id_fournisseur = models.ForeignKey('FOURNISSEUR', to_field='id_fournisseur', on_delete=models.CASCADE)
    fonctionnement_positionneur = models.ForeignKey('TYPEPOSITIONNEUR', to_field='id_fonctionnement_postionneur', on_delete=models.CASCADE)
    num_serie_positionneur = models.CharField(max_length=255, null=True, blank=True)
    signal_entre_positionneur = models.IntegerField(null=True, blank=True)
    signal_sortie = models.IntegerField(null=True, blank=True)
    repere_came = models.IntegerField(null=True, blank=True)
    face_came = models.IntegerField(null=True, blank=True)
    sens_action = models.CharField(max_length=255, null=True, blank=True)
    fermer_a = models.IntegerField(null=True, blank=True)
    ouvert_a = models.IntegerField(null=True, blank=True)
    type_positionneur = models.CharField(max_length=255, null=True, blank=True)
    presion_positionneur = models.CharField(max_length=255, null=True, blank=True)
    loi_positionneur = models.CharField(max_length=255, null=True, blank=True)
    tracker = FieldTracker()
  
class Vanne(models.Model):
    """
    Represents a valve in the system.
    """
    class Meta:
        db_table = 'VANNES'
    id_vanne = models.AutoField(primary_key=True, unique=True)
    id_atelier = models.ForeignKey('ATELIER', to_field='id_atelier', on_delete=models.CASCADE, null=True)
    repere_vanne = models.CharField(max_length=255, null=True, blank=True)
    affectation_vanne = models.CharField(max_length=255, null=True, blank=True)
    machine_vanne = models.CharField(max_length=255, null=True, blank=True)
    numero_commande = models.CharField(max_length=20, null=True, blank=True)
    id_actionneur = models.ForeignKey('ACTIONNEUR', to_field='id_actionneur', on_delete=models.CASCADE, null=True)
    id_corps = models.ForeignKey('CORPS', to_field='id_corps', on_delete=models.CASCADE, null=True)
    id_positionneur = models.ForeignKey('POSITIONNEUR', to_field='id_positionneur', on_delete=models.CASCADE, null=True, blank=True)
    id_fournisseur_vannes = models.ForeignKey('FOURNISSEUR', to_field='id_fournisseur', on_delete=models.CASCADE, default=0, null=True)
    type_vannes = models.CharField(max_length=255, null=True, blank=True)
    organe_reglant = models.CharField(max_length=255, null=True, blank=True)
    freq_revision = models.IntegerField(null=True, blank=True)
    derniere_revision = models.IntegerField(null=True, blank=True)
    voir_en = models.IntegerField(null=True, blank=True)
    en_service_vanne = models.IntegerField(default=1, blank=True)  # Si l'état est à 0, cela signifie que la vanne est bennée. Sinon, elle est toujours en service.
    date_commande = models.DateField(default=datetime.date(2001, 1, 1), null=True, blank=True)
    tracker = FieldTracker()


    def formatted_date_commande(self):
        return self.date_commande.strftime('%Y-%m-%d')
    
    #une méthode de type "toString"
   #def __str__(self) -> str:
       #return 'vannes' + self.nom_pizza + '(prix : ' + str(self.prixPizza) + '€)'

class REVISON(models.Model):
    class Meta:
        db_table = 'REVISION'
    id_revision = models.AutoField(primary_key=True, unique=True)
    id_revision_vanne =  models.IntegerField(null=True, blank=True, default=0)
    rev_id_vanne = models.IntegerField(null=True, blank=True, default=0)
    date_revision = models.DateField(default='2022-01-01')
    type_revision = models.CharField(max_length=255, null=True, blank=True, default='Aucun type')
    commentaire_revision = models.CharField(max_length=255, null=True, blank=True, default='Aucun commentaire')
    detail_commentaire = models.CharField( max_length=1500000,null=True, blank=True, default='Aucun détail')
    nom_technicien = models.CharField(max_length=255, null=True, blank=True, default='Aucun technicien')
    ajout_revision = models.CharField(max_length=255, null=True, blank=True, default='AUTO')
