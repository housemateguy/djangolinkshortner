from django.db import models
from django.utils import timezone
from app.models.link import Link

class Click(models.Model):
    link = models.ForeignKey(Link, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return self.timestamp.strftime('%Y-%m-%d %H:%M:%S')

    class Meta:
        ordering = ['-timestamp']