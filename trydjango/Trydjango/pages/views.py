from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args,**kwargs):
    print(request.user)
    #return HttpResponse("<h1>Hello world</h1>") #string of HTML code
    return render(request , "home.html",{})

def contact_view(request,*args,**kwargs):
    print(request.user)
    #return HttpResponse("<h1>contacts</h1>")
    return render(request,"contact.html",{})

def about_view(request,*args,**kwargs):
    #print(request.user)
    #return HttpResponse("<h1>contacts</h1>")
    my_context ={
        "my_text":"this is about us",
        "my_number": 123 ,
        "my_list":[123,456,789]
    }
    return render(request,"about.html",my_context)