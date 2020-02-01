from django.urls import path
from . import views

urlpatterns = [
	path('', views.post_list, name='post_list'), #post 
	]

	#this tells django where to go when URL is typed in


