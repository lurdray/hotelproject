from django.conf.urls import url
from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
	path("", views.indexView, name='index'),
	path("contact/", views.ContactView, name='contact'),	
	
	]
