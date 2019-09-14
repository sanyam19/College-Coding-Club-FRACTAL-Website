
from django.urls import path
from . import views

urlpatterns = [
			path('', views.question, name="explore"),
			path('questions/', views.question, name="questions"),
			
	       
	        path('filter/', views.filter, name="filter"),
            path('resources/', views.resources, name="resources"),
	        
]
