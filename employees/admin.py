from django.contrib import admin
from .models import Employee, EmployeeTerm, WorkPlace, Position
# Register your models here.

admin.site.register(Employee)
admin.site.register(EmployeeTerm)
admin.site.register(WorkPlace)
admin.site.register(Position)

