from django.contrib import admin
from django.urls import path
from . import views



#The path function is passed two arguments. 
#Two are required: 1. Route, 2. View
#Two are optional, 3. kwargs, 4. name


#ROUTE - this first goes to the URL given in poll/urls.py then the path here. 
#VIEW - when Django finds a matching pattern, it calls the specified view function with an HttpRequest object as the first argument and any 'captured' values from the list as keyword arguments
#KWARGS - Arbitrary kwargs can be passed in a dict to the target view
#NAME - Names the URL and allows you to refer to it directly from other parts in Django.



urlpatterns = [
 path('', views.index, name='index')
]