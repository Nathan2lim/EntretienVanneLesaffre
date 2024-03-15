
from django.contrib import admin
from django.urls import path
from appliVanne import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404, handler500



urlpatterns = [
    path("vannes/", views.listeVanne, name="vannes"),
    path("dump/", views.rechercheVanne, name="dump"),
    path("recherche/", views.rechercheAJAX),
    path("rechangeREG/", views.rechangeREG, name="rechangeREG"),
    path("rechangeTOR/", views.rechangeTOR, name="rechangeTOR"),
    path("actionneur/", views.actionneur, name="actionneur"),
    path("", views.listeVanne, name="home"),
    path('vanne/<int:id_vanne>/detail', views.detailVanne, name='detail_vanne'),
    path('vanne/<int:id_vanne>/detail_vanne', views.detailVanne, name='detail_vanne'),

    path('vanne/<int:id_vanne>/delete', views.delete, name='delete'),
    path('vanne/<int:id_vanne>/print', views.printer, name='print'),
    path('vanne/<int:id_vanne>/rechange', views.rechange, name='rechange'),
    path('vanne/<int:id_vanne>/recover', views.recover, name='recover'),
    path('vanne/<int:id_vanne>/recoverBIS', views.recoverBIS, name='recoverBIS'),
    path('vanne/<int:id_vanne>/edit', views.edit, name='edit'),
    path('vanne/<int:id_vanne>/commente', views.commente, name='comment'),

    path('vanne/<int:id_vanne>/revision', views.revision, name='revision'),
    path('vanne/<int:id_vanne>/traitement_revision', views.TraitementRevision, name='traitement_revision'),
    path('vanne/<int:id_revision>/detailrevision', views.detail_revision, name='detail_revision'),
    path('vanne/<int:id_vanne>/add_commentaire', views.add_commentaire, name='add_commentaire'),

    path('vanne/<int:id_vanne>/supprimerTotal', views.supressionTOTAL, name='supprimerTotal'),
    path("historique/", views.historiqueVanne, name="historique"),
    path("ajoutVanne/", views.ajoutVanne, name="ajoutVanne"),
    path("ajoutVanne/traitementAjoutVanne/", views.traitementAjoutVanne, name="traitementAjoutVanne"),
    path("ajoutVanne/traitementModifVanne/", views.traitementModifVanne, name="traitementModifVanne"),
    

]

handler404 = 'appliVanne.views.handler404'
handler500 = 'appliVanne.views.handler500'

