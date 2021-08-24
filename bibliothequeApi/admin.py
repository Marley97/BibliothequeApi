from django.contrib import admin
from .models import *

admin.site.register(Bibliothecaire)
admin.site.register(Categorie)
admin.site.register(Livre)
admin.site.register(Client)
admin.site.register(MesLivre)
admin.site.register(Vente)
