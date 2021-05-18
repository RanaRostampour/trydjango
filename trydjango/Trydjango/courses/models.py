from django.db import models
from django.urls import reverse

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length = 150)
    
def get_absolute_url(self):
    return reverse ("courses:courses_detail",kwargs={"id":self.id})