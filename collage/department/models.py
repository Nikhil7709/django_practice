from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100)
    established_date = models.DateField()
    
    def __str__(self):
        return self.name
    