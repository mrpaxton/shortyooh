from django.conf import settings
from django.db import models
from .utils import create_shortcode


SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)

class ShortURLManager(models.Manager):

    # get_object_or_404() calls _get_queryset() which receives manager.all()
    # overrding this all() method might affect the returned filtered value
    def all(self, *args, **kwargs):
        qs_main = super(ShortURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs

    def refresh_shortcodes(self, items=None):
        print(items)
        qs = ShortURL.objects.filter(id__gte=1)
        if items and isinstance(items, int):
            qs = qs.order_by('-id')[:items]
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.id)
            q.save()
            new_codes += 1
        return "New codes refreshed: {num}".format(num=new_codes)


class ShortURL(models.Model):
    objects = ShortURLManager()
    url = models.CharField(max_length=220, )
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True) #when model saved
    timestamp = models.DateTimeField(auto_now_add=True) #when model screated
    active = models.BooleanField(default=True)


    def save(self, *args, **kwargs):
        if not self.shortcode or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(ShortURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)
