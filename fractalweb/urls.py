from django.urls import path,include

from classroom import views
from extras import views
from . import views
urlpatterns = [
		path('', views.home,name="home"),
		path('classroom/', include('classroom.urls')),
		path('extra/', include('extras.urls')),
		path('announcements/', views.announcements,name="announcements"),
		path('about/', views.about,name="about"),
		path('login/', views.LogInView,name='login'),
		#path('userdetail/', vi ,name="userdetail"),
		
	        #'''path('filter/', views.filter,name='filter'),
               # path('login/', views.login,name='login'),
              #  path('signup/', views.signup,name='signup'), '''
]
