from django.urls import path
from django.contrib.auth import views as auth_views
from applicompte import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name = 'applicompte/login.html'), name = 'login'),
    path('logout/', views.deconnexion, name = 'logout'),
    path('connexion/', views.connexion),

]

