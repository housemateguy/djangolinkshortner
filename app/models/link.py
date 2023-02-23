import os
import random
import string
from django.db import models
from django.utils import timezone

class Link(models.Model):
    original_url = models.URLField()
    short_url = models.URLField(blank=True)
    token = models.CharField(max_length=6)
    clicks_count = models.PositiveIntegerField(default=0)
    max_clicks = models.PositiveIntegerField(default=0)
    expiration_date = models.DateTimeField(null=True, blank=True)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.original_url

    def generate_short_url(self):
        # generate a short URL based on the token and the domain
        domain = os.environ.get('DOMAIN', 'http://localhost:8000/')
        self.short_url = domain + self.token

    def is_expired(self):
        if self.expiration_date:
            return timezone.now() > self.expiration_date
        return False

    def is_click_limit_reached(self):
        return self.max_clicks > 0 and self.clicks_count >= self.max_clicks

    def generate_token(self):
        while True:
            token = ''.join(random.choices(string.ascii_uppercase 
                                           + string.ascii_lowercase + string.digits, k=6))
            if not Link.objects.filter(token=token).exists():
                self.token = token
                break
         
    class Meta:
        ordering = ['-creation_date']
