from django.forms import ModelForm
from django import forms
from .models import Employee,EmployeeTerm

class EmployeeForm(ModelForm):
    
    class Meta:
        model = Employee
        fields = '__all__'
        

class EmployeeTermForm(ModelForm):
    
    class Meta:
        model = EmployeeTerm
        fields = '__all__'
        widgets = {
            'startdate': forms.TimeInput(attrs={'type':'date'}),
        }
        


