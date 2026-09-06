from django import forms
from django.contrib.auth.models import User
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
            'product_id': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter unique numeric ID'}),
            'product_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Varsity Premium Hoodie'}),
            'product_price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': '0.00'}),
            'product_desc': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Provide product features and details...'}),
            'available_qty': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Available stock units'}),            
            'product_img': forms.FileInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
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




class SellerRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Create strong password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repeat your password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Choose unique username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@nuv.ac.in'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match. Please verify entries.")
        return cleaned_data


class SellerLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username or email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}))


