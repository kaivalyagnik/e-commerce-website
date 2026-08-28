from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Products
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from .models import Products
from .forms import ProductForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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

    db_products = Products.objects.filter(is_active=True)
    return render(request, 'women.html', {'products': db_products})

    return render(request, 'women.html')


def hats_view(request):
    return render(request, 'hats.html')

def accessories_view(request):
    return render(request, 'accessories.html')

def bags_view(request):
    return render(request, 'bags.html')

def drinkware_view(request):

    return render(request, 'drinkware.html')

@login_required(login_url='seller_login')
def seller_dashboard(request):
    return render(request, 'seller/dashboard.html')

@login_required(login_url='seller_login')
def seller_add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('seller_products')
    else:
        form = ProductForm()
    return render(request, 'seller/add_product.html', {'form': form})

@login_required(login_url='seller_login')
def seller_products(request):
    all_items = Products.objects.all().order_by('product_id')
    return render(request, 'seller/products_list.html', {'products': all_items})

@login_required(login_url='seller_login')
def seller_update_product(request, pk):
    product = get_object_or_404(Products, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('seller_products')
    else:
        form = ProductForm(instance=product)
    return render(request, 'seller/update_product.html', {'form': form, 'product': product})

    return render(request, 'drinkware.html')

def seller_login_view(request):
    if request.user.is_authenticated:
        return redirect('seller_dashboard') 
        
    if request.method == 'POST':
        user_name = request.POST.get('username')
        user_pass = request.POST.get('password')
        
        user = authenticate(request, username=user_name, password=user_pass)
        
        if user is not None:
            login(request, user)
            return redirect('seller_dashboard')
        else:
            messages.error(request, "Invalid username or password. Please try again.")
            return redirect('seller_login')
            
    return render(request, 'seller/login.html')

def seller_logout_view(request):
    logout(request)
    return redirect('seller_login')

