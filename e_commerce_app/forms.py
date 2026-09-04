
from django import forms
from .models import Products

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = [
            'product_id', 
            'product_title', 
            'product_price', 
            'product_desc', 
            'available_qty', 
            'product_img', 
            'is_active'
        ]
        widgets = {
            'product_id': forms.NumberInput(attrs={'class': 'form-input-field'}),
            'product_title': forms.TextInput(attrs={'class': 'form-input-field', 'placeholder': 'e.g., Varsity Hoodie'}),
            'product_price': forms.NumberInput(attrs={'class': 'form-input-field', 'step': '0.01'}),
            'product_desc': forms.Textarea(attrs={'class': 'form-input-field', 'rows': 3}),
            'available_qty': forms.NumberInput(attrs={'class': 'form-input-field'}),            
            'product_img': forms.FileInput(attrs={'class': 'form-file-field'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-checkbox-field'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        
        title = cleaned_data.get('product_title')
        desc = cleaned_data.get('product_desc')
        
        if title and str(title).isdigit():
            self.add_error('product_title', "Please enter a valid title.")
        
        if desc and str(desc).isdigit():
            self.add_error('product_desc', "Please enter a valid description.")
            
        return cleaned_data

