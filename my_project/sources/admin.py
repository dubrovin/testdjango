from django.contrib import admin

# Register your models here.
from .models import Source


class SourceAdmin(admin.ModelAdmin):

    class Meta:
        model = Source

admin.site.register(Source, SourceAdmin)