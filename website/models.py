from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Siteinfo(models.Model):
    titre_index = models.CharField(max_length=250)
    description_index = models.TextField()
    titre_dj = models.CharField(max_length=150)
    description_dj = models.TextField()
    titre_event = models.CharField(max_length=150)
    description_event = models.TextField()
    titre_about = models.CharField(max_length=150)
    description_about = models.TextField()
    titre_contact = models.CharField(max_length=150)
    description_contact = models.TextField()
    titre_dj = models.CharField(max_length=150, null=True)
    description_dj = models.TextField(null=True)
    titre_single = models.CharField(max_length=150, null=True)
    copyrights = models.CharField(max_length=150)
    about_footer_description = models.TextField()
    image_video_footer =models.ImageField(upload_to='image/footer')
    lien_video_footer = models.URLField(max_length=200)
    bg_index = models.ImageField(upload_to='background_index', null=True)

    date_add = models.DateTimeField( auto_now_add=True, null=True)
    date_update = models.DateTimeField(auto_now_add=True, null=True)
    status = models.BooleanField(default=True, blank=True)
    class Meta:
        verbose_name = "Siteinfo"
        verbose_name_plural = "Siteinfos"

    def __str__(self):
        return self.titre_index

class ReseauxSociau(models.Model):
    icons = [
        ('icon-facebook', 'facebook'),
        ('icon-twitter', 'twitter'),
        ('icon-instagram', 'instagram'),
        ('icon-linkedin', 'linkedin')
    ]
    nom = models.CharField(choices=icons, max_length=50)
    lien = models.URLField(max_length=200)
    created_by = models.ForeignKey(User, related_name='created_by_User', on_delete=models.CASCADE, null=True)
   

    date_add = models.DateTimeField( auto_now_add=True, null=True)
    date_update = models.DateTimeField(auto_now_add=True, null=True)
    status = models.BooleanField(default=True, blank=True)
    class Meta:
        verbose_name = "ReseauxSociau"
        verbose_name_plural = "ReseauxSociaux"
    def __str__(self):
        return self.nom
  
class Newletter(models.Model):
    email = models.EmailField(max_length=254)

    date_add = models.DateTimeField( auto_now_add=True, null=True)
    date_update = models.DateTimeField(auto_now_add=True, null=True)
    status = models.BooleanField(default=True, blank=True)
    class Meta:
        verbose_name = "Newletter"
        verbose_name_plural = "Newletters"

    def __str__(self):
        return self.email

class Contact(models.Model):
    full_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    subjects = models.CharField(max_length=250)
    message = models.TextField()

    date_add = models.DateTimeField( auto_now_add=True, null=True)
    date_update = models.DateTimeField(auto_now_add=True, null=True)
    status = models.BooleanField(default=True, blank=True)
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.full_name

class Contact_info(models.Model):
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=150)
    emailAdress = models.CharField(max_length=50)

    date_add = models.DateTimeField( auto_now_add=True, null=True)
    date_update = models.DateTimeField(auto_now_add=True, null=True)
    status = models.BooleanField(default=True, blank=True)
    class Meta:
        verbose_name = "Contact_info"
        verbose_name_plural = "Contact_infos"

    def __str__(self):
        return self.address

class About(models.Model):
    titre = models.CharField(max_length=250)
    description = models.TextField()
    lien = models.URLField(max_length=200)
    image = models.ImageField(upload_to='image/about')

    date_add = models.DateTimeField( auto_now_add=True, null=True)
    date_update = models.DateTimeField(auto_now_add=True, null=True)
    status = models.BooleanField(default=True, blank=True)
    class Meta:
        verbose_name = "About"
        verbose_name_plural = "Abouts"

    def __str__(self):
        return self.titre

class Our_team(models.Model):
    image = models.ImageField(upload_to='image/our_team')
    nom = models.CharField(max_length=150)
    description = models.TextField()
    fonction = models.CharField(max_length=50, null=True)

    date_add = models.DateTimeField( auto_now_add=True, null=True)
    date_update = models.DateTimeField(auto_now_add=True, null=True)
    status = models.BooleanField(default=True, blank=True)

    class Meta:
        verbose_name = "Our_team"
        verbose_name_plural = "Our_teams"

    def __str__(self):
        return self.nom

