from django.contrib import admin
from .models import Products
class ProductAdmin(admin.ModelAdmin):
        list_display = (
        'product_id', 
        'product_title', 
        'product_price', 
        'available_qty', 
        'is_active', 
        'created_at'
    )
        search_fields = (
        'product_id', 
        'product_title', 
        'product_desc'
    )
        list_filter = (
        'is_active', 
        'created_at', 
        'modified_at'
    )
        readonly_fields = ( 
        'created_at', 
        'modified_at'
    )
        fields = (
        'product_id',
        'product_title',
        'product_price',
        'available_qty',
        'product_desc',
        'product_img_url',
        'is_active',
        'created_at',
        'modified_at'
    )

admin.site.register(Products,ProductAdmin)

