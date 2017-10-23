from django.conf.urls import url
from PiLapser import views

urlpatterns = [
	url(r'^piLapse/$', views.get_totalImages, name='getTotalImages'),
	url(r'^$', views.HomePageView.as_view()),
]