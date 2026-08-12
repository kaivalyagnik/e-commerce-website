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
]
