from django.contrib import admin
from django.urls import include, path

from Blog.views import dynamic_lookup_view # Article_list_view
from Blog.views import (ArticleListView , ArticleDetailView ,
CreateView,ArticleCreateView,
ArticleUpdateView,ArticleDeleteView
)
app_name='Blog'
urlpatterns = [
    #path('<int:id>/',dynamic_lookup_view,name='articles'),
    #path('',Article_list_view,name='Article_list_view')
    path('',ArticleListView.as_view(),name='article_list') ,#ArticleListView is class base now
    path('<int:pk>/',ArticleDetailView.as_view(),name='article_detail'),
    path('create/',ArticleCreateView.as_view(),name='Create_article'),
    path('<int:pk>/update/',ArticleUpdateView.as_view(),name='article_update'),
    path('<int:pk>/delete/',ArticleDeleteView.as_view(),name='article_delete')
]
