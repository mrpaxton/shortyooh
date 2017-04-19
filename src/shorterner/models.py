from django.db import models
from utils import create_shortcode


class ShortURL(models.Model):
    url = models.CharField(max_length=220, )
    shortcode = models.CharField(max_length=15, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True) #when model saved
    timestamp = models.DateTimeField(auto_now_add=True) #when model screated

    def save(self, *args, **kwargs):
        if not self.shortcode or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(ShortURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)
