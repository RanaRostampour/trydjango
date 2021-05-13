from django import forms
from .models import Article

class BlogForm(forms.ModelForm):
    title = forms.CharField(max_length = 150)
    Date = forms.DateTimeField()
    class Meta:
        model = Article
        fields = ['title','Date']

