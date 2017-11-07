from django.conf.urls import url
from PiLapser import views

urlpatterns = [
	url(r'^piLapse/$', views.get_fields),
	url(r'^piLapse/fields$', views.fields),
	url(r'^piLapse/left$', views.move_left),
	url(r'^$', views.HomePageView.as_view()),
]
