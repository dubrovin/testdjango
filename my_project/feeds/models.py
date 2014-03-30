import requests
from django.db import models
from django.utils.encoding import smart_unicode
from lxml import etree
# Create your models here.

class Feed(models.Model):
    title = models.CharField(max_length=120, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    url = models.URLField(max_length=120, null=True, blank=True)

    def __unicode__(self):
        return smart_unicode(self.title)

    def save(self):
    	if(self.src):
    		resutl = requests.get(src)
    		super(Feed, self).save()