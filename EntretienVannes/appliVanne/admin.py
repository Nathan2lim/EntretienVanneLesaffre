from django.contrib import admin

# Register your models here.

from appliVanne.models import *

admin.site.register(Vanne)
admin.site.register(ATELIER)
admin.site.register(FOURNISSEUR)
admin.site.register(ACTIONNEUR)
admin.site.register(CORPS)
admin.site.register(TYPEPOSITIONNEUR)
admin.site.register(POSITIONNEUR)
admin.site.register(REVISON)
