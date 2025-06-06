from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_produits, name='liste_produits'),
    path('facture/creer/', views.creer_facture, name='creer_facture'),
    path('facture/<int:facture_id>/', views.detail_facture, name='detail_facture'),
    path('facture/<int:facture_id>/pdf/', views.facture_pdf, name='facture_pdf'),

]
