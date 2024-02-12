# SQLEditor export: Python Django Model
from django.db import models
  
class Atelier(models.Model): 
    idAtelier = models.IntegerField(primary_key=True, unique=True)
    nomAtelier = models.CharField(max_length=45)

  
class COMMANDE(models.Model): 
    idCommande = models.CharField(primary_key=True, unique=True, max_length=255)
    dateCommandee = models.CharField(max_length=3)

  
class FOURNISSEUR(models.Model): 
    idFournisseur = models.IntegerField(primary_key=True, unique=True)
    nomFournisseur = models.CharField(max_length=255)
    emailFournisseur = models.EmailField()
    telFournisseur = models.CharField(max_length=255)

  
class ACTIONNEUR(models.Model):
    idActionneur = models.IntegerField(primary_key=True, unique=True)
    idFournisseur = models.ForeignKey('FOURNISSEUR', to_field='idFournisseur', on_delete=models.CASCADE)
    numSeriActionneur = models.CharField(max_length=255, null=True)
    typeActionneur = models.CharField(max_length=255, null=True)
    tailleActionneur = models.IntegerField(null=True)
    typeContactActionneur = models.CharField(max_length=255, null=True)
    pressionAlimentation = models.CharField(max_length=255, null=True)
    sensActionneur = models.CharField(max_length=255, null=True)
    contactOuvFermActionneur = models.CharField(max_length=255, null=True)
    actionneurSimplDoubleEffet = models.CharField(max_length=255, null=True)
    commandeManuel = models.CharField(max_length=255, null=True)

  
class CORPS(models.Model): 
    idCorps = models.IntegerField(primary_key=True, unique=True)
    idFournisseur = models.ForeignKey('FOURNISSEUR', to_field='idFournisseur', on_delete=models.CASCADE)
    typeCorps = models.CharField(max_length=255)
    numSerieCorps = models.CharField(max_length=255)
    dnCorps = models.IntegerField()
    pnCorps = models.IntegerField()
    cvCorps = models.IntegerField()
    normeBrideCorps = models.CharField(max_length=255)
    codeCorps = models.CharField(max_length=255)
    matiereArbreCorps = models.CharField(max_length=255)
    matiereSiegeCorps = models.CharField(max_length=255)
    matiereOrgReglantCorps = models.CharField(max_length=255)
    corpsCorps = models.CharField(max_length=255)
    matiereGarnituresCorps = models.CharField(max_length=255)
    typeGarnitureCorps = models.CharField(max_length=255)

  
class TYPEPOSITIONNEUR(models.Model): 
    idFonctionnementPostionneur = models.IntegerField(primary_key=True, unique=True)
    descriptionTypePositionneur = models.CharField(max_length=255)
    typePositionneur = models.CharField(max_length=255)

  
class POSITIONNEUR(models.Model): 
    idPositionneur = models.IntegerField(primary_key=True, unique=True)
    idFournisseur = models.ForeignKey('FOURNISSEUR', to_field='idFournisseur', on_delete=models.CASCADE)
    fonctionnementPositionneur = models.ForeignKey('TYPEPOSITIONNEUR', to_field='idFonctionnementPostionneur', on_delete=models.CASCADE)
    numSeriePositionneur = models.CharField(max_length=255, null=True)
    signalEntrePositionneur = models.IntegerField(null=True)
    signalSortie = models.IntegerField(null=True)
    repereCame = models.IntegerField(null=True)
    faceCame = models.IntegerField(null=True)
    sensAction = models.IntegerField(null=True)
    femerA = models.IntegerField(null=True)
    ouvertA = models.IntegerField(null=True)
    typePositionneur = models.CharField(max_length=255, null=True)
    presionPositionneur = models.CharField(max_length=255, null=True)
    loiPositionneur = models.CharField(max_length=255, null=True)

  
class Vanne(models.Model): 
    idVanne = models.IntegerField(primary_key=True, unique=True)
    idAtelier = models.ForeignKey('Atelier', to_field='idAtelier', on_delete=models.CASCADE, null=True)
    repereVanne = models.CharField(max_length=255, null=True)
    affectationVanne = models.CharField(max_length=255, null=True)
    machineVanne = models.CharField(max_length=255, null=True)
    numeroCommande = models.CharField(max_length=20,null=True)
    idActionneur = models.ForeignKey('ACTIONNEUR', to_field='idActionneur', on_delete=models.CASCADE, null=True)
    idCorps = models.ForeignKey('CORPS', to_field='idCorps', on_delete=models.CASCADE, null=True)
    idPositionneur = models.ForeignKey('POSITIONNEUR', to_field='idPositionneur', on_delete=models.CASCADE, null=True)
    idFournisseurVannes = models.ForeignKey('FOURNISSEUR', to_field='idFournisseur', on_delete=models.CASCADE, default=0, null=True)
    typeVannes = models.CharField(max_length=255, null=True)
    organeReglant = models.CharField(max_length=255, null=True)
    dateAchat = models.CharField(max_length=255, null=True)
    freqRevision = models.IntegerField(null=True)
    derniereRevision = models.IntegerField(null=True)
    voirEn = models.IntegerField(null=True)

