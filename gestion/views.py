from django.shortcuts import render, get_object_or_404, redirect
from .models import Produit, Facture
from django.core.paginator import Paginator

def liste_produits(request):
    produits = Produit.objects.all().order_by('nom')
    paginator = Paginator(produits, 5)  # 5 produits par page
    page = request.GET.get('page')
    produits_page = paginator.get_page(page)
    return render(request, 'gestion/liste_produits.html', {'produits': produits_page})

def creer_facture(request):
    if request.method == 'POST':
        ids_produits = request.POST.getlist('produits')
        facture = Facture.objects.create()
        facture.produits.set(ids_produits)
        return redirect('detail_facture', facture_id=facture.id)
    
    produits = Produit.objects.all()
    return render(request, 'gestion/creer_facture.html', {'produits': produits})

def detail_facture(request, facture_id):
    facture = get_object_or_404(Facture, id=facture_id)
    total = facture.total()
    return render(request, 'gestion/detail_facture.html', {'facture': facture, 'total': total})

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def facture_pdf(request, facture_id):
    facture = get_object_or_404(Facture, id=facture_id)
    total = facture.total()

    template = get_template("gestion/facture_pdf.html")
    html = template.render({"facture": facture, "total": total})

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"attachment; filename=facture_{facture.id}.pdf"

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse("Erreur lors de la génération du PDF")
    return response
