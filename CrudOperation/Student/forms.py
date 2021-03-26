from django import forms
from .models import Employee
from django.contrib.auth.forms import UserCreationForm

class EmployeeForm(forms.ModelForm):
    Firstname = forms.CharField()
    lastname = forms.TextInput()
    email = forms.EmailField()



    class Meta:
        model = Employee
        fields = ['Firstname','lastname','email']


    def clean(self):
        cleaned_data = super(EmployeeForm, self).clean()
        return cleaned_data