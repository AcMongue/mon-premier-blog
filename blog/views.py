from django.shortcuts import render,get_object_or_404
from django.utils import timezone  # Importation de timezone pour gérer les dates et heures
from .models import Article  # Importation du modèle Article pour interagir avec la base de données
from .forms import ArticleForm  # Importation du formulaire ArticleForm pour créer ou modifier des articles
from django.shortcuts import redirect  # Importation de redirect pour rediriger l'utilisateur vers une autre page après une action réussie
# Create your views here.
def liste_article(request): # Vue pour afficher la liste des articles,le paramètre request est l'objet de requête HTTP qui contient des informations sur la requête effectuée par l'utilisateur.
    articles=Article.objects.filter(date_publication__lte=timezone.now()).order_by('date_publication') # Récupère tous les articles dont la date de publication est inférieure ou égale à la date actuelle, triés par date de publication croissante.
    return render(request,'blog/liste_article.html',{'articles':articles}) #la fonction render est utilisée pour rendre un template HTML, ici on rend le template 'blog/liste_article.html', le premier paramètre est l'objet de requête, le deuxième paramètre est le nom du template à rendre.
# Cette vue est associée à la route définie dans blog/urls.py, elle sera appelée lorsque l'utilisateur accède à la route correspondante.

def detail_article(request,pk): # Vue pour afficher le détail d'un article, le paramètre id est l'identifiant de l'article à afficher.
    article=get_object_or_404(Article,pk=pk) # Récupère l'article dont l'identifiant correspond à l'id passé en paramètre, si l'article n'existe pas, renvoie une erreur 404.
    return render(request,'blog/detail_article.html',{'article':article}) # Rendu du template 'blog/detail_article.html' avec l'article récupéré, le paramètre 'article' est passé au template pour afficher les détails de l'article.
# Cette vue est associée à la route définie dans blog/urls.py, elle sera appelée lorsque l'utilisateur accède à la route avec un identifiant d'article spécifique.

def nouvel_article(request):
    if request.method == 'POST': #Vérification de si la méthode de la requête est post
        form = ArticleForm(request.POST) # Si la méthode de la requête est POST, cela signifie que l'utilisateur a soumis le formulaire pour créer un nouvel article.
        if form.is_valid(): # Vérifie si le formulaire est valide, c'est-à-dire si tous les champs requis sont remplis correctement.
            article = form.save(commit=False) # Crée une instance de l'article à partir des
            # données du formulaire, mais ne le sauvegarde pas encore dans la base de données.
            article.auteur = request.user # Assigne l'utilisateur actuel comme auteur de l'article.
            article.date_creation = timezone.now()
            article.date_publication = timezone.now() # Définit la date de création et de publication de l'article à la date et heure actuelles
            article.save() # Sauvegarde l'article dans la base de données.
            return redirect('blog/detail_article', pk=article.pk) # Redirige l'utilisateur vers la page de détail de l'article nouvellement créé, en utilisant son identifiant (pk).
    else:
        # Si la méthode de la requête n'est pas POST, cela signifie que l'utilisateur accède à la page pour créer un nouvel article.
        # On crée une instance vide du formulaire ArticleForm pour afficher le formulaire vide.
        # Le formulaire sera affiché dans le template 'blog/nouvel_article.html'.
        # Le paramètre 'form' est passé au template pour afficher le formulaire de création d'article.
     # Vue pour créer un nouvel article, le paramètre request est l'objet de requête HTTP.
        form=ArticleForm() # Création d'une instance du formulaire ArticleForm, qui est un formulaire basé sur le modèle Article.
    return render(request,'blog/nouvel_article.html',{'form':form}) # Rendu du template 'blog/nouvel_article.html' avec le formulaire, le paramètre 'form' est passé au template pour afficher le formulaire de création d'article.

def modifier_article(request, pk):
    article = get_object_or_404(Article, pk=pk)  # Récupère l'article à modifier en fonction de son identifiant (pk).
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)  # Si la méthode de la requête est POST, on crée une instance du formulaire ArticleForm avec les données soumises et l'article existant.
        if form.is_valid():  # Vérifie si le formulaire est valide.
            article = form.save(commit=False)  # Crée une instance de l'article à partir des données du formulaire, mais ne le sauveg
            article.auteur = request.user  # Assigne l'utilisateur actuel comme auteur de l'article.
            article.date_creation = timezone.now()  # Définit la date de création de l'article à la date et heure actuelles.
            article.date_publication = timezone.now()  # Définit la date de publication de l'article à la date et heure actuelles.
            # Si l'article a déjà une date de publication, on la garde inchangée.
            form.save()  # Sauvegarde les modifications apportées à l'article.
            return redirect('blog/detail_article', pk=article.pk)  # Redirige vers la page de détail de l'article modifié.
    else:
        form = ArticleForm(instance=article)  # Si la méthode de la requête n'est pas POST, on crée une instance du formulaire ArticleForm avec l'article existant pour pré-remplir le formulaire.
    return render(request, 'blog/nouvel_article.html', {'form': form})  # Rendu du template 'blog/modifier_article.html' avec le formulaire pour modifier l'article.