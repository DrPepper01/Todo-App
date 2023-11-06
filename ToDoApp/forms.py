from django import forms
from .models import Category


class AddCategoryForm(forms.ModelForm):

    name = forms.CharField(label='Category name')

    class Meta:
        model = Category
        fields = '__all__'


