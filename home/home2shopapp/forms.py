from django import forms

from home2shopapp.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class EditImage(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['photo']