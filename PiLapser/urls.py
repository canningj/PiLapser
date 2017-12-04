from django.conf.urls import url
from PiLapser import views

urlpatterns = [
	url(r'^piLapse/$', views.get_fields),
	url(r'^move_pos/$', views.move_pos),
	url(r'^move_neg/$', views.move_neg),
    url(r'^status/$', views.status),
    url(r'^get_status/$', views.render_status),
    url(r'^completed/$', views.completion),
    url(r'^error/$', views.camera_error),
    url(r'^cancel/$', views.cancel),

]
