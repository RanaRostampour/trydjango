from django.db import models
from django.urls import reverse

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length = 150)
    Date = models.DateTimeField(blank=True)
    
    def get_absolute_url(self):
        return reverse ("Blog:article_detail",kwargs={"pk":self.pk})
