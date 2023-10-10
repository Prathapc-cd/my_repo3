from django.db import models

class Mobile(models.Model):
    brand= models.CharField(max_length=50)
    cost= models.CharField(max_length=50)
    searchablefields=['brand','cost']
 
def __str__(self):
    return f"{self.brand} {self.cost}"