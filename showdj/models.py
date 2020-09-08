from django.db import models
from django.contrib.auth.models import User
# Create your models here
class Show(models.Model):
    image = models.ImageField(upload_to='image/shows')
    titre = models.CharField(max_length=150)
    description = models.TextField()
    musique = models.URLField(max_length=200)
    created_by = models.ForeignKey(User, related_name='show_created', on_delete=models.CASCADE, null='true')

    date_add = models.DateTimeField( auto_now_add=True, null=True)
    date_update = models.DateTimeField(auto_now_add=True, null=True)
    status = models.BooleanField(default=True, blank=True)
    
    class Meta:
        verbose_name = "Show"
        verbose_name_plural = "Shows"

    def __str__(self):
        return self.titre

