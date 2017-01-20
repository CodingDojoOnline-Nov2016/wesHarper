from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^users/(?P<user_id>\d+)$', views.show),
]