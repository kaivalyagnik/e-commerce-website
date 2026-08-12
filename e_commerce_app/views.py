from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Products

# # Create your views here.
# def show_invoices(request):
#     return HttpResponse("Your invoice page.")

# def navigation_view(request):
#     return render(request, 'nav.html')

# class AboutPageView(TemplateView):
#     template_name = 'nav.html'

def index_view(request):

    return render(request, 'index.html')

def men_view(request):
    db_products = Products.objects.filter(is_active=True)
    return render(request, 'men.html', {'products': db_products})

def women_view(request):
    return render(request, 'women.html')

def hats_view(request):
    return render(request, 'hats.html')

def accessories_view(request):
    return render(request, 'accessories.html')

def bags_view(request):
    return render(request, 'bags.html')

def drinkware_view(request):
    return render(request, 'drinkware.html')