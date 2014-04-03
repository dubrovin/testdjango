# from io import StringIO, BytesIO
import requests
import pdb;
from django.conf import settings
from django.db import models
from django.utils.encoding import smart_unicode
from lxml import etree, objectify
# from django.http import HttpRequest
# Create your models here.

class Feed(models.Model):
    title = models.CharField(max_length=120, null=True, blank=True)
    text = models.TextField(null=True)
    create_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    url = models.URLField(max_length=120, null=True, blank=True)
    file = models.FileField(upload_to=settings.MEDIA_ROOT, null=True, blank=True)

    def __unicode__(self):
        return smart_unicode(self.title)

class Source(models.Model):
    title = models.CharField(max_length=120, null=True, blank=True)
    src = models.URLField(max_length=120, null=True, blank=True)
    file = models.FileField(upload_to=settings.MEDIA_ROOT, null=True, blank=True)

    def __unicode__(self):
        return smart_unicode(self.title)

    def save(self):
        if self.src:
            data = etree.parse(self.src)
            ns_map = {'ns': 'http://www.w3.org/2005/Atom'}

            nodes = data.xpath('//ns:feed/ns:entry', namespaces=ns_map)

            for node in nodes:
                title = node.xpath('.//ns:title', namespaces=ns_map)[0].text
                text = node.xpath('.//ns:content', namespaces=ns_map)[0].text
                create_at = node.xpath('.//ns:published', namespaces=ns_map)[0].text
                url = node.xpath('.//ns:id', namespaces=ns_map)[0].text

                f = Feed.objects.create(title=title, text=text, create_at=create_at, url=url)
                f.save()
                super(Source, self).save()
        elif self.file:
            data = etree.parse(self.file.read())
            ns_map = {'ns': 'http://www.w3.org/2005/Atom'}

            nodes = data.xpath('//ns:feed/ns:entry', namespaces=ns_map)

            for node in nodes:
                title = node.xpath('.//ns:title', namespaces=ns_map)[0].text
                text = node.xpath('.//ns:content', namespaces=ns_map)[0].text
                create_at = node.xpath('.//ns:published', namespaces=ns_map)[0].text
                url = node.xpath('.//ns:id', namespaces=ns_map)[0].text

                f = Feed.objects.create(title=title, text=text, create_at=create_at, url=url)
                f.save()
                super(Source, self).save()
        
