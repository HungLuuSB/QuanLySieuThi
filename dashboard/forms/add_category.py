from django import forms

class AddCategoryForm(forms.Form):
    category_name = forms.CharField(max_length=50)
