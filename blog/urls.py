from django.urls import path, include
from . import views

urlpatterns=[
    path('', views.liste_article, name='blog/liste_article'), # Route pour la liste des articles
    path('article/<int:pk>/', views.detail_article, name='blog/detail_article'), # Route pour le détail d'un article
]