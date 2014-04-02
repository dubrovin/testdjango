from django.conf.urls import patterns, url

from feeds.views import FeedListView, FeedDetailView

urlpatterns = patterns('',
    url(r'^$', FeedListView.as_view(), name='feed-list'),
    url(r'^(?P<pk>[-_\w]+)/$', FeedDetailView.as_view(), name='feed-detail')
)