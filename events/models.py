from django.db import models

# Create your models here.

class Event(models.Model):
    image = models.ImageField(upload_to='image/events')
    date = models.DateTimeField(auto_now_add=False)
    titre = models.CharField( max_length=250)

    date_add = models.DateTimeField( auto_now_add=True, null=True)
    date_update = models.DateTimeField(auto_now_add=True, null=True)
    status = models.BooleanField(default=True, blank=True)
    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return self.titre


