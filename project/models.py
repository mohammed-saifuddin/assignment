
from django.db import models
from django.core.exceptions import ValidationError
from rest_framework import viewsets


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('T', 'Transgender')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    department = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name
    
    def clean(self):
        if self.age > 60:
            raise ValidationError("Employee age cannot be more than 60.")
        if self.gender not in [choice[0] for choice in self.GENDER_CHOICES]:
            raise ValidationError("Gender should be M, F, or T.")

    
 



