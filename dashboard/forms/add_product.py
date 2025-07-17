from django import forms


class AddProductForm(forms.Form):
    product_name = forms.CharField(max_length=30)
    product_desc = forms.CharField(max_length=50)
    product_price = forms.DecimalField(max_digits=5, decimal_places=2)
    stock = forms.IntegerField(min_value=0)
    category = forms.IntegerField()
