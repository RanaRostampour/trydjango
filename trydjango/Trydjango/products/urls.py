
from django.contrib import admin
from django.urls import path , include
#own
from pages.views import home_view, contact_view ,about_view
from products.views import Product_detail_view 
from products.views import Product_create_view,dynamic_lookup_view
from products.views import product_delete_view, product_list_view

app_name = 'product'
urlpatterns = [

    
    path('',product_list_view, name='Product_list'),
    path('create/',Product_create_view,name='Product_create'),
    path('<int:id>/',dynamic_lookup_view,name='Products'),
    path('<int:id>/delete/',product_delete_view,name='product_delete'),
    path('<int:id>',Product_detail_view,name='Product_detail_view')
]
