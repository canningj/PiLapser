from django.conf.urls import url
from PiLapser import views

urlpatterns = [
	url(r'^piLapse/$', views.get_stepCount, name='getTotalImages'),
	url(r'^piLapse/move$', views.get_move),
	url(r'^$', views.HomePageView.as_view()),
]
