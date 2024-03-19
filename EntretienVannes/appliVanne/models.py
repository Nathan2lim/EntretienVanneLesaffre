# SQLEditor export: Python Django Model
from django.db import models
import datetime
from django.utils import formats
from applicompte.models import *
from model_utils import FieldTracker
from datetime import datetime


from django.db import models
from model_utils import FieldTracker

class ATELIER(models.Model):
    class Meta:
        db_table = 'ATELIER'
    id_atelier = models.AutoField(primary_key=True, unique=True, verbose_name="ID de l'atelier")
    nom_atelier = models.CharField(max_length=45, default='a remplir', unique=True, verbose_name="Nom de l'atelier")

class FOURNISSEUR(models.Model): 
    class Meta:
        db_table = 'FOURNISSEUR'
    id_fournisseur = models.AutoField(primary_key=True, unique=True, verbose_name="ID du fournisseur")
    nom_fournisseur = models.CharField(max_length=255, verbose_name="Nom du fournisseur")
    email_fournisseur = models.EmailField(verbose_name="Adresse e-mail du fournisseur")
    tel_fournisseur = models.CharField(max_length=255, verbose_name="Numéro de téléphone du fournisseur")

class ACTIONNEUR(models.Model):
    class Meta:
        db_table = 'ACTIONNEUR'


        
    id_actionneur = models.AutoField(primary_key=True, unique=True, verbose_name="ID de l'actionneur")
    id_fournisseur = models.ForeignKey('FOURNISSEUR', to_field='id_fournisseur', on_delete=models.CASCADE, verbose_name="ID du fournisseur")
    num_serie_actionneur = models.CharField(max_length=255, null=True, blank=True, verbose_name="Numéro de série de l'actionneur")
    type_actionneur = models.CharField(max_length=255, null=True, blank=True, verbose_name="Type de l'actionneur")
    taille_actionneur = models.CharField(max_length=255, null=True, blank=True, verbose_name="Taille de l'actionneur")
    type_contact_actionneur = models.CharField(max_length=255, null=True, blank=True, verbose_name="Type de contact de l'actionneur")
    pression_alimentation = models.CharField(max_length=255, null=True, blank=True, verbose_name="Pression d'alimentation de l'actionneur")
    sens_actionneur = models.CharField(max_length=255, null=True, blank=True, verbose_name="Sens de l'actionneur")
    contact_ouv_ferm_actionneur = models.CharField(max_length=255, null=True, blank=True, verbose_name="Contact ouverture/fermeture de l'actionneur")
    actionneur_simpl_double_effet = models.CharField(max_length=255, null=True, blank=True, verbose_name="Actionneur simple/double effet")
    commande_manuel = models.CharField(max_length=255, null=True, blank=True, verbose_name="Commande manuelle de l'actionneur")
    tracker = FieldTracker()

class CORPS(models.Model): 
    class Meta:
        db_table = 'CORPS'
    id_corps = models.AutoField(primary_key=True, unique=True, verbose_name="ID du corps")
    id_fournisseur = models.ForeignKey('FOURNISSEUR', to_field='id_fournisseur', on_delete=models.CASCADE, verbose_name="ID du fournisseur")
    type_corps = models.CharField(max_length=255,null=True, blank=True, verbose_name="Type de corps")
    num_serie_corps = models.CharField(max_length=255,null=True, blank=True, verbose_name="Numéro de série du corps")
    dn_corps = models.CharField(max_length=255,null=True, blank=True, verbose_name="DN du corps")
    pn_corps = models.CharField(max_length=255,null=True, blank=True, verbose_name="PN du corps")
    cv_corps = models.CharField(max_length=255,null=True, blank=True, verbose_name="CV du corps")
    norme_bride_corps = models.CharField(max_length=255,null=True, blank=True, verbose_name="Norme de bride du corps")
    code_corps = models.CharField(max_length=255,null=True, blank=True, verbose_name="Code du corps")
    matiere_arbre_corps = models.CharField(max_length=255,null=True, blank=True, verbose_name="Matière de l'arbre du corps")
    matiere_siege_corps = models.CharField(max_length=255,null=True, blank=True, verbose_name="Matière du siège du corps")
    matiere_org_reglant_corps = models.CharField(max_length=255,null=True, blank=True, verbose_name="Matière de l'organe réglant du corps")
    corps_corps = models.CharField(max_length=255,null=True, blank=True, verbose_name="Corps du corps")
    matiere_garnitures_corps = models.CharField(max_length=255,null=True, blank=True, verbose_name="Matière des garnitures du corps")
    type_garniture_corps = models.CharField(max_length=255,null=True, blank=True, verbose_name="Type de garniture du corps")
    tracker = FieldTracker()

class TYPEPOSITIONNEUR(models.Model): 
    class Meta:
        db_table = 'TYPEPOSITIONNEUR'


        
    id_fonctionnement_postionneur = models.AutoField(primary_key=True, unique=True, verbose_name="ID du type de positionneur")
    description_type_positionneur = models.CharField(max_length=255, blank=True, verbose_name="Description du type de positionneur")
    type_positionneur = models.CharField(max_length=255, blank=True, verbose_name="Type de positionneur")

class POSITIONNEUR(models.Model): 
    class Meta:
        db_table = 'POSITIONNEUR'


        
    id_positionneur = models.AutoField(primary_key=True, unique=True, verbose_name="ID du positionneur")
    id_fournisseur = models.ForeignKey('FOURNISSEUR', to_field='id_fournisseur', on_delete=models.CASCADE, verbose_name="ID du fournisseur")
    fonctionnement_positionneur = models.ForeignKey('TYPEPOSITIONNEUR', to_field='id_fonctionnement_postionneur', on_delete=models.CASCADE, verbose_name="Fonctionnement du positionneur",null=True, blank=True)
    num_serie_positionneur = models.CharField(max_length=255, null=True, blank=True, verbose_name="Numéro de série du positionneur")
    signal_entre_positionneur = models.IntegerField(null=True, blank=True, verbose_name="Signal d'entrée du positionneur")
    signal_sortie = models.IntegerField(null=True, blank=True, verbose_name="Signal de sortie du positionneur")
    repere_came = models.IntegerField(null=True, blank=True, verbose_name="Repère de la came du positionneur")
    face_came = models.IntegerField(null=True, blank=True, verbose_name="Face de la came du positionneur")
    sens_action = models.CharField(max_length=255, null=True, blank=True, verbose_name="Sens d'action du positionneur")
    fermer_a = models.IntegerField(null=True, blank=True, verbose_name="Fermer à du positionneur")
    ouvert_a = models.IntegerField(null=True, blank=True, verbose_name="Ouvert à du positionneur")
    type_positionneur = models.CharField(max_length=255, null=True, blank=True, verbose_name="Type de positionneur")
    presion_positionneur = models.CharField(max_length=255, null=True, blank=True, verbose_name="Pression du positionneur")
    loi_positionneur = models.CharField(max_length=255, null=True, blank=True, verbose_name="Loi du positionneur")
    tracker = FieldTracker()

class Vanne(models.Model):
    class Meta:
        db_table = 'VANNES'


        
    id_vanne = models.AutoField(primary_key=True, unique=True, verbose_name="ID de la vanne")
    id_atelier = models.ForeignKey('ATELIER', to_field='id_atelier', on_delete=models.CASCADE, null=True, verbose_name="ID de l'atelier")
    repere_vanne = models.CharField(max_length=255, null=True, blank=True, verbose_name="Repère de la vanne")
    affectation_vanne = models.CharField(max_length=255, null=True, blank=True, verbose_name="Affectation de la vanne")
    machine_vanne = models.CharField(max_length=255, null=True, blank=True, verbose_name="Machine de la vanne")
    numero_commande = models.CharField(max_length=20, null=True, blank=True, verbose_name="Numéro de commande")
    id_actionneur = models.ForeignKey('ACTIONNEUR', to_field='id_actionneur', on_delete=models.CASCADE, null=True, verbose_name="ID de l'actionneur")
    id_corps = models.ForeignKey('CORPS', to_field='id_corps', on_delete=models.CASCADE, null=True, verbose_name="ID du corps")
    id_positionneur = models.ForeignKey('POSITIONNEUR', to_field='id_positionneur', on_delete=models.CASCADE, null=True, blank=True, verbose_name="ID du positionneur")
    id_fournisseur_vannes = models.ForeignKey('FOURNISSEUR', to_field='id_fournisseur', on_delete=models.CASCADE, default=0, null=True, verbose_name="ID du fournisseur de vannes")
    type_vannes = models.CharField(max_length=255, null=True, blank=True, verbose_name="Type de vannes")
    organe_reglant = models.CharField(max_length=255, null=True, blank=True, verbose_name="Organe réglant")
    freq_revision = models.IntegerField(null=True, blank=True, verbose_name="Fréquence de révision")
    derniere_revision = models.IntegerField(null=True, blank=True, verbose_name="Date de la dernière révision")
    voir_en = models.IntegerField(null=True, blank=True, verbose_name="Date de la prochaine révision")
    en_service_vanne = models.IntegerField(default=1, blank=True, verbose_name="En service")
    date_commande = models.DateField(null=True, blank=True, verbose_name="Date de la commande")
    tracker = FieldTracker()

class REVISON(models.Model):
    class Meta:
        db_table = 'REVISION'
        
    id_revision = models.AutoField(primary_key=True, unique=True, verbose_name="ID de la révision")
    id_revision_vanne =  models.IntegerField(null=True, blank=True, default=0, verbose_name="ID de la révision de la vanne")
    rev_id_vanne = models.IntegerField(null=True, blank=True, default=0, verbose_name="ID de la vanne")
    date_revision = models.DateTimeField(null=True, blank=True, verbose_name="Date de la révision")
    type_revision =  models.ForeignKey('TYPEREVISION', to_field='id_type_revision', on_delete=models.CASCADE, null=True, verbose_name="ID du  type de revision")
    commentaire_revision = models.CharField(max_length=255, null=True, blank=True, default='Aucun commentaire', verbose_name="Commentaire de révision")
    detail_commentaire = models.CharField( max_length=1500000,null=True, blank=True, default='Aucun détail', verbose_name="Détail de révision")
    nom_technicien = models.CharField(max_length=255, null=True, blank=True, default='Aucun technicien', verbose_name="Nom du technicien")
    ajout_revision = models.CharField(max_length=255, null=True, blank=True, default='AUTO', verbose_name="Ajout de révision")

class TypeRevision(models.Model):
    class Meta:
        db_table = 'TYPEREVISION'
    id_type_revision = models.AutoField(primary_key=True, unique=True, verbose_name="ID du type de révision")
    type_revision = models.CharField(max_length=255, blank=True, verbose_name="Type de révision")