# 💼 Générateur de Factures – Projet Django

Une application web simple en Django permettant de :
- Gérer des produits (CRUD)
- Créer des factures avec plusieurs produits
- Afficher le total à payer
- Télécharger la facture en PDF
- Interface claire avec Bootstrap

## 🖼️ Aperçu

![Liste produits](./captures/liste_produits.png)
![Création facture](./captures/creer_facture.png)
![PDF](./captures/pdf_facture.png)

## 🚀 Technologies utilisées

- Django 5.2
- Bootstrap 5
- HTML/CSS
- xhtml2pdf

## 🔧 Installation

```bash
git clone 
cd facture-django
python -m venv env
env\Scripts\activate  # sous Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
