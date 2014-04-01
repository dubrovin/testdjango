# from io import StringIO, BytesIO
import requests
import pdb;
from django.db import models
from django.utils.encoding import smart_unicode
from lxml import etree, objectify
# from django.http import HttpRequest
# Create your models here.

class Feed(models.Model):
    title = models.CharField(max_length=120, null=True, blank=True)
    #text = models.TextField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    url = models.URLField(max_length=120, null=True, blank=True)
    file = models.FileField(upload_to='/static/media/', null=True)

    def __unicode__(self):
        return smart_unicode(self.title)

    # def save(self):
    # 	if(self.src):
    # 		resutl = requests.get(src)
    # 		super(Feed, self).save()

class Source(models.Model):
    title = models.CharField(max_length=120, null=True, blank=True)
    src = models.URLField(max_length=120, null=True, blank=True)

    def __unicode__(self):
        return smart_unicode(self.title)

    def save(self):
        if self.src:
            result = requests.get(self.src)
            parser = etree.XMLParser(ns_clean=True)
            #root = etree.parse(result.text, parser)
            root = etree.fromstring(result.text.encode('utf-8'), parser)
            objectify.deannotate(root, cleanup_namespaces=True)
            # str = etree.tostring(root.getchild())
            list_of_feeds = []
            for r in root:
                if('entry' in r.tag):
                    list_of_feeds.append(r)
            for feed in list_of_feeds:
                buf = Feed.objects.create(title=feed[1].text, create_at=feed[5].text, url=feed[3].text)
                #pdb.set_trace()
                buf.save()
            super(Source, self).save()
