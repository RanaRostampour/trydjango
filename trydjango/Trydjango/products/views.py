from django.shortcuts import render
#21
from .models import Product

def Product_detail_view(requests):
    obj = Product.objects.get(id=1)
    # context ={
    #   'title':obj.title,
    #   'summary':obj.summary
    # }  
    
    context = {
        'object':obj
    }
    return render(requests,"product/detail.html",context)
