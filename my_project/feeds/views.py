from django.shortcuts import render

# Create your views here.

from django.views.generic.list import ListView
from django.utils import timezone

from feeds.models import Feed

class FeedListView(ListView):

    model = Feed
    template_name = "feeds/feed_list.html"

    def get_context_data(self, **kwargs):
        context = super(FeedListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context