from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employee
from .forms import EmployeeForm




# Create your views here.

def index(request):

    employees = Employee.objects.all()
    print(employees)
    context = {
        'employees':employees
    }

    return render(request,'employees/index.html',context)

def add(request):

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


    # return HttpResponse(f'el id es {id}')

