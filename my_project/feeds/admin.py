from django.contrib import admin

# Register your models here.
from .models import Feed


class FeedAdmin(admin.ModelAdmin):

    class Meta:
        model = Feed

admin.site.register(Feed, FeedAdmin)
