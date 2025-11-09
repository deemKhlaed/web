from django.db import models

# Create your models here.

class Address(models.Model):  
    city = models.CharField(max_length=30)
    def __str__(self):
        return f"{self.city}"
    
class Student(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.age}"