from django.forms import ModelForm
from .models import Employee, EmployeeTerm, Position ,WorkPlace


class EmployeeForm(ModelForm):
    
    class Meta:
        model = Employee
        fields = '__all__'

