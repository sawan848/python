from django.urls import path
from . import views
#/products
#/products/1/details
#/products/new



urlpatterns=[
    path('',views.index,name='index'),
    path('new',views.new )

]