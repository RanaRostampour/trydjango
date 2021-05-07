
from django.shortcuts import render
#21

from .forms import ProductForm,RawProductForm
from .models import Product

#def Product_create_view(request):
#    my_form = RawProductForm()
#    if request.method =="POST":
#        my_form = RawProductForm(request.POST) #(request.POST) to make sure its entered
#        if my_form.is_valid():
#            #now the data is good
#            print(my_form.cleaned_data)
#            Product.objects.create(**my_form.cleaned_data)  #to save clean data in DB
#            my_form = RawProductForm()  #to clean Form
#        else:
#            print(my_form.errors)   #describe errors(usully dosen't need)
#    context ={
#        "form": my_form
#    }
#    return render(request,"product/Product_create.html",context)

def Product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    
    context={
        'form':form
    }
    return render(request, "product/Product_create.html",context)

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
