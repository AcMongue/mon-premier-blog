from django.db import models #ici on importe le module models de Django qui permet de créer des modèles de données pour l'application.
from django.conf import settings #on importe le module settings de Django qui permet d'accéder aux paramètres de configuration de l'application.
from django.utils import timezone #on importe le module timezone de Django qui permet de gérer les dates et heures dans l'application.
# Create your models here.

class Article(models.Model): #création d'un modèle de données pour les articles de blog, on hérite de la classe Models
    auteur=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #on crée une clé étrangère vers le modèle utilisateur de Django, on_delete=models.CASCADE signifie que si l'utilisateur est supprimé, tous les articles associés seront également supprimés et settings.AUTH_USER_MODEL permet de référencer le modèle utilisateur configuré dans les paramètres de Django.
    titre=models.CharField(max_length=500) #Champ pour le titre avec une taille maximale de 500 caractères
    texte_article=models.TextField() #Champ pour le contenu de l'article qui est un textField sans taille définie
    date_creation=models.DateTimeField(default=timezone.now) #on crée un champ de date et heure avec une valeur par défaut de la date et heure actuelle.
    date_publication=models.DateTimeField(blank=True, null=True) #on crée un champ de date et heure qui peut être vide ou nul, ce champ est utilisé pour la date de publication de l'article.
    

    def publication(self): #methode pour publier l'article, elle met à jour la date de publication avec la date et heure actuel
    #le self fait référence à l'instance actuelle de l'article.
        self.date_publication = timezone.now()
        self.save()

    def __str__(self): #méthode spéciale pour retourner une représentation en chaîne de caractères de l'article, ici on retourne le titre de l'article.
        return f"{self.titre}, Rédigé par  {self.auteur.username}" #on retourne le titre de l'article et le nom d'utilisateur de l'auteur, self.auteur.username permet d'accéder au nom d'utilisateur de l'auteur de l'article.