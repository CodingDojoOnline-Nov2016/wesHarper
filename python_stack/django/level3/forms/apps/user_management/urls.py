from django.conf.urls import url
from . import views

app_name = "users"

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^login$', views.login, name='login'),
	url(r'^create$', views.create, name='create'),
	url(r'^logout$', views.logout, name='logout'),
]