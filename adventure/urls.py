from django.conf.urls import url
from . import api, views
from .views import RoomViewSet


urlpatterns = [
    url('init', api.initialize),
    url('move', api.move),
    url('say', api.say),
    url('rooms/', RoomViewSet.as_view(), name="rooms-all")
]
