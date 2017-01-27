from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^process/(?P<location>[a-z]+)$', views.process, name='process'),
	url(r'^save$', views.save, name='save'),
	url(r'^show$', views.show, name='show'),
]