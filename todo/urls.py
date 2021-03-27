from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
 
    path('',views.home,name="home"),
    url('about',views.about,name="about"),
    path('delete/<int:id>',views.delete,name="delete"),
    url('tasklist',views.TaskList.as_view(),name='tasklist'),

  
]
