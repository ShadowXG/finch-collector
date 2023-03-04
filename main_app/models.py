from django.db import models
from django.urls import reverse

# Create your models here.

class Finch(models.Model):
    species = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.species
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={ 'finch_id': self.id })