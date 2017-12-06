from django.conf.urls import url
from PiLapser import views

urlpatterns = [
	url(r'^piLapse/$', views.get_fields), #display fields for a new timelapse
	url(r'^move_pos/$', views.move_pos), #move slider in the positive direction
	url(r'^move_neg/$', views.move_neg), #move slider in the negative direction
    url(r'^status/$', views.status), #retrieve status of a current timelapse
    url(r'^get_status/$', views.render_status), #display retrieved status
    url(r'^completed/$', views.completion), #show when timelapse completed
    url(r'^error/$', views.camera_error), #display when camera is not plugged in
    url(r'^cancel/$', views.cancel), #send a cancel request to abort timelapse
]
