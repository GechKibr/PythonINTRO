from django import forms

from .models  import Product


class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = [
		'title',
		'price',
		'featured',
		'summary',
		'description',
		]




class RawProductForm(forms.Form):
	title = forms.CharField()
	price = forms.DecimalField()
	description = forms.CharField()
