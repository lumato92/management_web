
from django.db import models
from django.utils.timezone import now

# Create your models here.

class Position(models.Model):
    name = models.CharField(blank=False,null=False, max_length=50)
    description = models.TextField(blank=False,null=True)

    def __str__(self):
        return self.name
    

class WorkPlace(models.Model):
    name = models.CharField(max_length=100,blank=False,null=False)
    adress = models.CharField(max_length= 100,blank=False,null=False)
    phone =  models.IntegerField(blank=False,null=False)

    def __str__(self):
        return self.name
    

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,blank=False,null=False)
    lastname = models.CharField(max_length=50,blank=False,null=False)
    dob = models.DateField(blank=False,null=False,)
    adress = models.CharField(max_length=100,blank=False,null=False)
    nationality = models.CharField(max_length=50, blank=False,null=False)
    dni = models.IntegerField(blank=False,null=False)
    cuil = models.IntegerField(blank=False,null=False)
    mobile = models.IntegerField(blank=False,null=False)
    phone = models.IntegerField(blank=True,null=True)
    position = models.ForeignKey(Position,on_delete=models.CASCADE) #Relacion uno a muchos
    salary = models.IntegerField(blank=False,null=False)
    active = models.BooleanField()
    place = models.ForeignKey(WorkPlace,on_delete=models.CASCADE)




    def __str__(self):
        return str(self.id)
    

class EmployeeTerm (models.Model):
    id = models.AutoField(primary_key=True)
    employee_id = models.ForeignKey(Employee,on_delete=models.CASCADE)
    salary = models.IntegerField(blank=False,null=False)
    startdate = models.DateTimeField(blank=False,null=False)
    # enddate = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.id
    