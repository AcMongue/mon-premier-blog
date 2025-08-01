from django.urls import path, include
from . import views

urlpatterns=[
    path('', views.liste_article, name='blog/liste_article'), # Route pour la liste des articles
    path('article/<int:pk>/', views.detail_article, name='blog/detail_article'), # Route pour le détail d'un article
    path('article/nouvel', views.nouvel_article, name='blog/nouvel_article'), # Route pour créer un nouvel article
    path('article/<int:pk>/modifier/', views.modifier_article, name='blog/nouvel_article'), # Route pour modifier un article
]