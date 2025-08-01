from django.shortcuts import render
from django.utils import timezone  # Importation de timezone pour gérer les dates et heures
from .models import Article  # Importation du modèle Article pour interagir avec la base de données

# Create your views here.
def liste_article(request): # Vue pour afficher la liste des articles,le paramètre request est l'objet de requête HTTP qui contient des informations sur la requête effectuée par l'utilisateur.
    articles=Article.objects.filter(date_publication__lte=timezone.now()).order_by('date_publication') # Récupère tous les articles dont la date de publication est inférieure ou égale à la date actuelle, triés par date de publication croissante.
    return render(request,'blog/liste_article.html',{'articles':articles}) #la fonction render est utilisée pour rendre un template HTML, ici on rend le template 'blog/liste_article.html', le premier paramètre est l'objet de requête, le deuxième paramètre est le nom du template à rendre.
# Cette vue est associée à la route définie dans blog/urls.py, elle sera appelée lorsque l'utilisateur accède à la route correspondante.
