from django.shortcuts import render

# Create your views here.
def liste_article(request): # Vue pour afficher la liste des articles,le paramètre request est l'objet de requête HTTP qui contient des informations sur la requête effectuée par l'utilisateur.
    return render(request,'blog/liste_article.html') #la fonction render est utilisée pour rendre un template HTML, ici on rend le template 'blog/liste_article.html', le premier paramètre est l'objet de requête, le deuxième paramètre est le nom du template à rendre.
# Cette vue est associée à la route définie dans blog/urls.py, elle sera appelée lorsque l'utilisateur accède à la route correspondante.