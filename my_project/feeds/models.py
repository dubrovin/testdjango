from django.db import models
from django.utils.encoding import smart_unicode
# Create your models here.

class Feed(models.Model):
    title = models.CharField(max_length=120, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    src = models.URLField(max_length=120, null=True, blank=True)

    def __unicode__(self):
        return smart_unicode(self.title)
