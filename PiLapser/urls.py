from django.conf.urls import url
from PiLapser import views

urlpatterns = [
	url(r'^piLapse/$', views.get_fields),
	url(r'^piLapse/fields$', views.fields),
	url(r'^$', views.HomePageView.as_view()),
]
