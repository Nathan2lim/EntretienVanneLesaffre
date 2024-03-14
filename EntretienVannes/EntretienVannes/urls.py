
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500
from appliVanne import views




urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include('appliVanne.urls')),
    path('',include('applicompte.urls')),
    path('tinymce/', include('tinymce.urls')),  
]

handler404 = 'appliVanne.views.handler404'
handler500 = 'appliVanne.views.handler500'
