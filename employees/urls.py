from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='employees'),
    path('add/',views.add, name='add_employee'),
    path("details/<int:id>",views.details, name="employee_details"),
    path("edit/<int:id>",views.edit, name="employee_edit"),
    path("salary/<int:id>",views.salary,name='salary')
]
