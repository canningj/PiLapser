from django.conf.urls import url
from PiLapser import views

urlpatterns = [
	url(r'^piLapse/$', views.get_TotalImages, name='getTotalImages'),
	url(r'^$', views.HomePageView.as_view()),
]