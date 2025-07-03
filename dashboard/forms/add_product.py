from django import forms


class AddProductForm(forms.Form):
    product_name = forms.CharField(max_length=30)
    product_desc = forms.CharField(max_length=50)
    category = forms.IntegerField()
