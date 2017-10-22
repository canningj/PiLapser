from django.conf.urls import url
from PiLapser import views

urlpatterns = [
	url(r'^$', views.HomePageView.as_view()),
]