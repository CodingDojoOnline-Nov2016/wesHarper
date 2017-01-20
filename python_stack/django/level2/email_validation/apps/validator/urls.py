from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^success$', views.success),
	url(r'^process$', views.process),
	url(r'^user/(?P<id>\d+)/delete', views.destroy),
]