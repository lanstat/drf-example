from django.urls import path

from .views import TrackList, TrackDetail, PlaylistList, PlaylistDetail, PlaylistContentList, PlaylistContentDetail
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^tracks/$', TrackList.as_view()),
    url(r'^tracks/(?P<pk>[0-9]+)/$', TrackDetail.as_view()),
    url(r'^playlist/$', PlaylistList.as_view()),
    url(r'^playlist/(?P<pk>[0-9]+)/$', PlaylistDetail.as_view()),
    url(r'^playlist/(?P<pk>[0-9]+)/tracks/$', PlaylistContentList.as_view()),
    url(r'^playlist/(?P<pk>[0-9]+)/tracks/(?P<trackPk>[0-9]+)/$', PlaylistContentDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)