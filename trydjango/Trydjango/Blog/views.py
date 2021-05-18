from django.shortcuts import render

# Create your views here.
from .models import Article
from .Forms import BlogForm
from django.shortcuts import get_object_or_404,redirect
#37
from django.views.generic import(
    CreateView,DetailView,ListView,UpdateView,DeleteView
)
#38
from .Forms import BlogForm

from django.urls import reverse

class ArticleCreateView(CreateView):
    template_name = 'Blog/Article_create.html'
    form_class = BlogForm
    queryset = Article.objects.all()
    
    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)
        #success_url = '/'    
        
    ##def get_success_url(self):
    ##  return '/'



#def Article_view(request):
#   obj = Article.objects.get
#  return render(request,"Blog/Article_detail.html")

#def Article_list_view(request):
#    queryset = Article.objects.all() #list of objects
#    context={
#        "object_list":queryset
#    }
#    return render (request,"Blog/Article_list.html",context)

def dynamic_lookup_view(request,id):
    obj = get_object_or_404(Article, id=id)
    
    context = {
        "object":obj
    }
    return render(request,"Blog/Article_detail.html",context)


def Article_create_view(request):
    form = BlogForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = BlogForm()
    
    context={
        'form':form
    }
    return render(request, "Blog/Article_form.html",context)

class ArticleListView(ListView):
    template_name = 'Blog/Article_list.html'
    queryset = Article.objects.all() #<Blog>/<modelname>_list.html
    
class ArticleDetailView(DetailView):
    template_name = 'Blog/Article_detail.html'
    queryset = Article.objects.all() 

    
class ArticleUpdateView (UpdateView):
    template_name = 'Blog/Article_create.html'
    form_class = BlogForm
    queryset = Article.objects.all()
    
    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)
        success_url = '/' 
        
        
class ArticleDeleteView(DeleteView):
    template_name = 'Blog/Article_delete.html'
    queryset = Article.objects.all()
    
    def get_success_url(self):
        return reverse("Blog:article_list")
