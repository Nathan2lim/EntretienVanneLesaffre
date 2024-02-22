# SQLEditor export: Python Django Model
from django.db import models
  
class ATELIER(models.Model):
    class Meta:
        db_table = 'ATELIER'
         
    id_atelier = models.IntegerField(primary_key=True, unique=True)
    nom_atelier = models.CharField(max_length=45, default='a remplir', unique=True)
   
class COMMANDE(models.Model): 
    class Meta:
        db_table = 'COMMANDE'
        
    id_commande = models.CharField(primary_key=True, unique=True, max_length=255)
    date_commandee = models.CharField(max_length=3)

  
class FOURNISSEUR(models.Model): 
    class Meta:
        db_table = 'FOURNISSEUR'
        
    id_fournisseur = models.IntegerField(primary_key=True, unique=True)
    nom_fournisseur = models.CharField(max_length=255)
    email_fournisseur = models.EmailField()
    tel_fournisseur = models.CharField(max_length=255)

  
class ACTIONNEUR(models.Model):
    
    class Meta:
        db_table = 'ACTIONNEUR'
        
    id_actionneur = models.IntegerField(primary_key=True, unique=True)
    id_fournisseur = models.ForeignKey('FOURNISSEUR', to_field='id_fournisseur', on_delete=models.CASCADE)
    num_serie_actionneur = models.CharField(max_length=255, null=True)
    type_actionneur = models.CharField(max_length=255, null=True)
    taille_actionneur = models.IntegerField(null=True)
    type_contact_actionneur = models.CharField(max_length=255, null=True)
    pression_alimentation = models.CharField(max_length=255, null=True)
    sens_actionneur = models.CharField(max_length=255, null=True)
    contact_ouv_ferm_actionneur = models.CharField(max_length=255, null=True)
    actionneur_simpl_double_effet = models.CharField(max_length=255, null=True)
    commande_manuel = models.CharField(max_length=255, null=True)

  
class CORPS(models.Model): 
    class Meta:
        db_table = 'CORPS'
        
    id_corps = models.IntegerField(primary_key=True, unique=True)
    id_fournisseur = models.ForeignKey('FOURNISSEUR', to_field='id_fournisseur', on_delete=models.CASCADE)
    type_corps = models.CharField(max_length=255)
    num_serie_corps = models.CharField(max_length=255)
    dn_corps = models.IntegerField()
    pn_corps = models.IntegerField()
    cv_corps = models.IntegerField()
    norme_bride_corps = models.CharField(max_length=255)
    code_corps = models.CharField(max_length=255)
    matiere_arbre_corps = models.CharField(max_length=255)
    matiere_siege_corps = models.CharField(max_length=255)
    matiere_org_reglant_corps = models.CharField(max_length=255)
    corps_corps = models.CharField(max_length=255)
    matiere_garnitures_corps = models.CharField(max_length=255)
    type_garniture_corps = models.CharField(max_length=255)

  
class TYPEPOSITIONNEUR(models.Model): 
    
    class Meta:
        db_table = 'TYPEPOSITIONNEUR'
        
    id_fonctionnement_postionneur = models.IntegerField(primary_key=True, unique=True)
    description_type_positionneur = models.CharField(max_length=255)
    type_positionneur = models.CharField(max_length=255)

  
class POSITIONNEUR(models.Model): 
    
    class Meta:
        db_table = 'POSITIONNEUR'
        
    id_positionneur = models.IntegerField(primary_key=True, unique=True)
    id_fournisseur = models.ForeignKey('FOURNISSEUR', to_field='id_fournisseur', on_delete=models.CASCADE)
    fonctionnement_positionneur = models.ForeignKey('TYPEPOSITIONNEUR', to_field='id_fonctionnement_postionneur', on_delete=models.CASCADE)
    num_serie_positionneur = models.CharField(max_length=255, null=True)
    signal_entre_positionneur = models.IntegerField(null=True)
    signal_sortie = models.IntegerField(null=True)
    repere_came = models.IntegerField(null=True)
    face_came = models.IntegerField(null=True)
    sens_action = models.IntegerField(null=True)
    femer_a = models.IntegerField(null=True)
    ouvert_a = models.IntegerField(null=True)
    type_positionneur = models.CharField(max_length=255, null=True)
    presion_positionneur = models.CharField(max_length=255, null=True)
    loi_positionneur = models.CharField(max_length=255, null=True)

  
class Vanne(models.Model):
    """
    Represents a valve in the system.
    """
    class Meta:
        db_table = 'VANNES'
    id_vanne = models.IntegerField(primary_key=True, unique=True)
    id_atelier = models.ForeignKey('ATELIER', to_field='id_atelier', on_delete=models.CASCADE, null=True)
    repere_vanne = models.CharField(max_length=255, null=True)
    affectation_vanne = models.CharField(max_length=255, null=True)
    machine_vanne = models.CharField(max_length=255, null=True)
    numero_commande = models.CharField(max_length=20, null=True)
    id_actionneur = models.ForeignKey('ACTIONNEUR', to_field='id_actionneur', on_delete=models.CASCADE, null=True)
    id_corps = models.ForeignKey('CORPS', to_field='id_corps', on_delete=models.CASCADE, null=True)
    id_positionneur = models.ForeignKey('POSITIONNEUR', to_field='id_positionneur', on_delete=models.CASCADE, null=True)
    id_fournisseur_vannes = models.ForeignKey('FOURNISSEUR', to_field='id_fournisseur', on_delete=models.CASCADE, default=0, null=True)
    type_vannes = models.CharField(max_length=255, null=True)
    organe_reglant = models.CharField(max_length=255, null=True)
    date_achat = models.CharField(max_length=255, null=True)
    freq_revision = models.IntegerField(null=True)
    derniere_revision = models.IntegerField(null=True)
    voir_en = models.IntegerField(null=True)
    en_service_vanne = models.IntegerField(default=1)  # Si l'état est à 0, cela signifie que la vanne est bennée. Sinon, elle est toujours en service.
    
    #une méthode de type "toString"
   #def __str__(self) -> str:
       #return 'vannes' + self.nom_pizza + '(prix : ' + str(self.prixPizza) + '€)'
