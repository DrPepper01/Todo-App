from django import forms
from .models import Category, ToDo


class AddCategoryForm(forms.ModelForm):

    name = forms.CharField(label='Category name')

    class Meta:
        model = Category
        fields = '__all__'

        widget = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }


class AddTodoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ('title', 'content', 'created', 'expiration_date', 'category')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.TextInput(attrs={'class': 'form-control'}),
            'created': forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                                                      'class': 'form-control'}),
            'expiration_date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                                                      'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control form-control-lg  select'})
        }


# class UpdateTodoForm(forms.ModelForm):
#
#     class Meta:
#         model = ToDo
#         fields = ('title', 'content', 'created', 'expiration_date', 'category')
