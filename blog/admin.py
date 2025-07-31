from django.contrib import admin
from .models import Article #on importe le modèle Article depuis le fichier models.py de l'application blog.



# Register your models here.
admin.site.register(Article) #on enregistre le modèle Article dans l'interface d'administration de Django, cela permet de gérer les articles de blog depuis l'interface d'administration.
# Cela permet de gérer les articles de blog depuis l'interface d'administration.