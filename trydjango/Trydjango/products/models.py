from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120) # max_length = required
    price = models.DecimalField(decimal_places=2,max_digits=1000, default=0)
    featured = models.BooleanField() #null=True or default =True
    summary = models.TextField(help_text="use keyboard",blank=True,null=True)