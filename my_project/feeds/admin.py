from django.contrib import admin

# Register your models here.
from .models import Feed
from .models import Source

class FeedAdmin(admin.ModelAdmin):

    class Meta:
        model = Feed

admin.site.register(Feed, FeedAdmin)

class SourceAdmin(admin.ModelAdmin):

    class Meta:
        model = Source

admin.site.register(Source, SourceAdmin)