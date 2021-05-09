from django.db import models
from django.urls import reverse
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120) # max_length = required
    price = models.DecimalField(decimal_places=2,max_digits=1000, default=0)
    featured = models.BooleanField(default=True) #null=True or default =True
    summary = models.TextField(help_text="!",blank=True,null=True)
    
#33
    def get_absoulute_url(self):
        return reverse ("product:Products",kwargs={"id":self.id}) #return f"/products/{self.id}/"