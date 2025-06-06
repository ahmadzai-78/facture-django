# 💼 Générateur de Factures – Projet Django

Une application web simple en Django permettant de :

- ✅ Gérer des produits (CRUD)
- ✅ Créer des factures avec plusieurs produits
- ✅ Afficher le total à payer
- ✅ Télécharger la facture au format PDF
- ✅ Interface claire et responsive grâce à Bootstrap

---

## 🚀 Technologies utilisées

- Django 5.2
- Bootstrap 5
- HTML / CSS
- xhtml2pdf (pour générer des PDF)

---

## 🔧 Installation locale

```bash
git clone https://github.com/ahmadzai-78/facture-django.git
cd facture-django
python -m venv env
env\Scripts\activate       # (sous Windows)
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


