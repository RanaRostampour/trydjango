from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    title =forms.CharField(label='Title', widget=forms.TextInput(attrs={"placeholder":"your title"})) 
    summary =forms.CharField(required=False,widget=forms.Textarea(attrs={"class":"new-class-two","rows":5,"cols":25,"id":"summary_area"}))   
    price = forms.DecimalField(initial=199.99) #copied from below    
    email = forms.EmailField()
    
    class  Meta:
        model = Product
        fields =[
            'title',
            'summary',
            'price'
        ]
        
    #making clean form 
    #def clean_<my_field_name>
    def clean_title(self,*args,**kwargs):
        title = self.cleaned_data.get("title")
        if not "CFE" in title:
            raise forms.ValidationError("this is not a valid title")
        return title
    def clean_email(self,*args,**kwargs):   #this won't save in DB
        email =self.cleaned_data.get("email")
        if not email.endswith(".com"):
            raise forms.ValidationError("this is not a valid email")
        return email
    
class RawProductForm(forms.Form):
    title =forms.CharField(label='Title', widget=forms.TextInput(attrs={"placeholder":"your title"})) 
    summary =forms.CharField(required=False,widget=forms.Textarea(attrs={"class":"new-class-two","rows":5,"cols":25,"id":"summary_area"}))   #it's True by default
    price = forms.DecimalField(initial=199.99)
        