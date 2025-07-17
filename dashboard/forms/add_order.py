from django import forms

class AddOrderForm(forms.Form):
    customer_name = forms.CharField(max_length=30, required=True)
    customer_phone = forms.CharField(max_length=11, required=True)
    shipping_address = forms.CharField(widget=forms.Textarea, required=True)
    grand_total = forms.DecimalField(max_digits=50, decimal_places=2, required=True)
    status = forms.CharField()