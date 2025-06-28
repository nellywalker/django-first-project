from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('personnes/', views.person_list, name='person_list'),
    path('personnes/ajouter/', views.person_create, name='person_create'),
    path('personnes/modifier/<int:pk>/', views.person_update, name='person_update'),
    path('personnes/supprimer/<int:pk>/', views.person_delete, name='person_delete'),
]
