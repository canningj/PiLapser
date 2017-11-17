from django.conf.urls import url, include
from rest_framework import routers
from .views import timelapseViewSet, move_pos, move_neg, get_fields
router = routers.DefaultRouter(trailing_slash=False)
router.register("tlParams", timelapseViewSet)

urlpatterns = [
	#url(r'^piLapse/$', views.get_fields),
	url(r'^move_pos/$', move_pos),
	url(r'^move_neg/$', move_neg),
	url(r'^api/', include(router.urls)),
	url(r'^run_timelapse/$', get_fields),

]
