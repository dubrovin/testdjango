from io import StringIO, BytesIO
import requests
import pdb;
from django.db import models
from django.utils.encoding import smart_unicode
from lxml import etree
# from django.http import HttpRequest
# Create your models here.

class Source(models.Model):
    title = models.CharField(max_length=120, null=True, blank=True)
    src = models.URLField(max_length=120, null=True, blank=True)

    def __unicode__(self):
        return smart_unicode(self.title)

    def save(self):
    	if self.src:
    		result = requests.get(self.src)
    		root = etree.fromstring(result.text.encode('utf-8'), base_url="http://www.w3.org/2005/Atom")
    		l = []
    		for r in root.getchildren():
				l.append(r.tag)
    		pdb.set_trace()
    		super(Source, self).save()
