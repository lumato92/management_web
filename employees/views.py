from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employee ,EmployeeTerm
from .forms import EmployeeForm, EmployeeTermForm




# Create your views here.

def index(request):

# RETURN THE FULL LIST OF EMPLOYEES

    employees = Employee.objects.all()
    print(employees)
    context = {
        'employees':employees
    }

    return render(request,'employees/index.html',context)

def add(request):

# Add a new employee 

    if(request.method == 'GET'):
        form = EmployeeForm()
        context = {
            'form':form,
            
        }

        return render(request,'employees/form.html',context)
   
    if(request.method == 'POST'):
        form = EmployeeForm(request.POST)
        form.save()

        return redirect('employees')


def details(request, id):
    """Show details of the Employee

    Args:
        request (): HTTP request GET
        id (int): Id reffered to the employee

    Returns:
        Html template: Full info of employee
    """
    employee = Employee.objects.get(id=id)
    print(employee)
    context = {
        'employee':employee
    }

    return render(request,'employees/details.html',context)


def edit(request, id):

    employee = Employee.objects.get(id=id)

    if(request.method =='GET'):
        employee = Employee.objects.get(id=id)
        form = EmployeeForm(instance=employee)

        context = {
            'id':id,
            'form':form
        }

        return  render(request,'employees/edit.html',context)
    
    if(request.method =='POST'):
        
        form = EmployeeForm(request.POST,instance=employee)
        form.save()

        return redirect('employees')


def salary(request,id):
    
    if(request.method =='GET'):
        
        employee = Employee.objects.get(id=id)
        
        data = {
            'employee_id':employee.id,
        }
        salary = EmployeeTermForm(data)
        
        
        
        context = {
            'employee':employee,
            'salary':salary,
            'id':id
        }
        
        
        return render(request,'employees/salary.html',context)
    
    if(request.method =='POST'):
        
        form = EmployeeTermForm(request.POST)
        form.save()
        
        employee = Employee.objects.get(id=id)
        employee.salary =request.POST.get('salary')
        employee.save()

        return redirect('employees')
