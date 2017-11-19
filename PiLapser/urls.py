from django.conf.urls import url
from PiLapser import views

urlpatterns = [
	url(r'^index.html$', views.move_pos),
	url(r'^piLapse/$', views.get_fields),
	url(r'^move_pos/$', views.move_pos),
	url(r'^move_neg/$', views.move_neg),
]
