from django.conf.urls import url
from .views import RouteView, UltraView

app_name = "routes"

urlpatterns = [
	url(r'^$', RouteView.as_view()),
	url(r'^ultra$', UltraView.as_view()),
	url(r'^whatever$', UltraView.as_view(statement="whatever")),
]