# Create your models here.
from django.db import models

class Produit(models.Model):
    nom = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_peremption = models.DateField()

    def __str__(self):
        return self.nom

class Facture(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    produits = models.ManyToManyField(Produit)

    def total(self):
        return sum(produit.prix for produit in self.produits.all())

    def __str__(self):
        return f"Facture #{self.id} - {self.date.strftime('%d/%m/%Y')}"
