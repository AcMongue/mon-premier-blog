from django import forms
from .models import Article  # Importation du modèle Article pour interagir avec la base de données

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article  # Spécifie le modèle à utiliser pour le formulaire
        fields = ['titre', 'texte_article']  # Liste des champs du modèle à inclure dans le formulaire
        