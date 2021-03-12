from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
 
class Location(models.Model):
    location = models.CharField(max_length=64, default='Location')
    description = models.TextField(default='Type the description here')
    name = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
 
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('locations_details', args=[str(self.id)])