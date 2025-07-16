from django.db import models


class Student:
  def _init_(self, name, age, height):
     self .name=name
     self .age =age
     self.height =height
  def greet(self):
     print("Hello welcome to this class. My name is {self.name} and i am {self.age} years old")
     
# class users(models.Model):
#   full_name=models.CharField(max_length=100)
#   email=models.EmailField(unique=True)
#   password=models.CharField(max_length=100)
#   phone=models.CharField(max_length=15, blank=True, null=True)
#   address=models.TextField(blank=True, null=True)
#   birth_date = models.DateTimeField(auto_now =True)
# # Create your models here.
# #this is a home page = this-is-home -page

# class Products(models.Model):
#   STATUS= [
#      ('p', "pending"),
#      ('C', "Completed"),
#      ('F', "Failed"),
#   ]
#   name =models.CharField(max_length=100)
#   slug = models.SlugField(unique=True)
#   description = models.TextField()
#   price =models.DecimalField(max_digits =10 , decimal_place=2)
#   inventory =models.IntegerField(default=0)
#   created_at =models.DateField(auto_now_add=True)
#   status = models.CharField(max_length=1, choices= STATUS, default ='p')