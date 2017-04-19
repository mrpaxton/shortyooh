from django.db import models
import random
import string


def code_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class ShortURL(models.Model):
    url = models.CharField(max_length=220, )
    shortcode = models.CharField(max_length=15, unique=True)
    updated = models.DateTimeField(auto_now=True) #when model saved
    timestamp = models.DateTimeField(auto_now_add=True) #when model screated

    def save(self, *args, **kwargs):
        self.shortcode = code_generator()
        super(ShortURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)
