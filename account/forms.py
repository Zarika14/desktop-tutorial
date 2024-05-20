from django import forms
from django.core.exceptions import ValidationError
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'description', 'price']

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        category = cleaned_data.get('category')
        description = cleaned_data.get('description')
        price = cleaned_data.get('price')

        if Product.objects.filter(name=name, category=category, description=description, price=price).exists():
            raise ValidationError('A product with the same name, category, description, and price already exists.')

        return cleaned_data


class ProductFilterForm(forms.Form):
    name = forms.CharField(required=False, label='Product Name')
    category = forms.ModelChoiceField(
        queryset=ProductCategory.objects.all(),
        required=False,
        label='Category'
    )

class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['quantity']