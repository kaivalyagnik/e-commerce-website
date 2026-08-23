from django.urls import path
from e_commerce_app import views
from e_commerce_app import admin

urlpatterns = [
    path('', views.index_view, name='index'),
    path('men/', views.men_view, name='men'),
    path('women/', views.women_view, name='women'),
    path('hats/', views.hats_view, name='hats'),
    path('accessories/', views.accessories_view, name='accessories'),
    path('bags/', views.bags_view, name='bags'),
    path('drinkware/', views.drinkware_view, name='drinkware'),
    path('seller/', views.seller_dashboard, name='seller_dashboard'),
    path('seller/products/', views.seller_products, name='seller_products'),
    path('seller/products/add/', views.seller_add_product, name='seller_add_product'),
    path('seller/products/update/<int:pk>/', views.seller_update_product, name='seller_update_product'),
]
