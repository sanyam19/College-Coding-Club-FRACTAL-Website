from django.urls import path
from . import views
app_name='classroom'
urlpatterns = [
		#path('', views.home,name="home"),
			path('', views.classroom, name="classroom"),
	        path('question/', views.question, name="question"),
	        path('slide/', views.slide, name="slide"),
	        path('archive/', views.archive, name="archive"),
	        path('schedule/', views.schedule, name="schedule"),
	        
]
