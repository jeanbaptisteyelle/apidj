from django.contrib import admin

# Register your models here.
from . import models 

from django.utils.safestring import mark_safe

from actions.actions import Action

@admin.register(models.Siteinfo)
class SiteinfoAdmin(Action):
    list_display = ('titre_index','titre_dj','titre_dj','titre_dj','titre_event','date_add','date_update','status','image_video_footer_view','bg_index_view')
    list_filter = ('date_add','date_update','status')
    search_fields = ('titre_index',)
    date_hierarchy = 'date_add'
    list_display_links = ['titre_index']
    fieldsets = [
    ('Siteinfo_infos', {'fields':['titre_index','description_index','titre_event','description_event','titre_about','description_about','titre_contact','description_contact','titre_dj','description_dj','titre_single','copyrights','about_footer_description','image_video_footer','lien_video_footer','bg_index']}),
    ('standard', {'fields':['status']}),
    ]

    
    def bg_index_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.bg_index.url))
    
    def image_video_footer_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.image_video_footer.url))
    


@admin.register(models.ReseauxSociau)
class ReseauxSociauAdmin(Action):
    list_display = ('nom','date_add','date_update','status')
    list_filter = ('date_add','date_update','status')
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    fieldsets = [
    ('ReseauxSociau_infos', {'fields':['nom','lien','created_by']}),
    ('standard', {'fields':['status']}),
    ]

@admin.register(models.Newletter)
class NewletterAdmin(Action):
    list_display = ('email','date_add','date_update','status')
    list_filter = ('date_add','date_update','status')
    search_fields = ('email',)
    date_hierarchy = 'date_add'
    list_display_links = ['email']
    fieldsets = [
    ('Newletter_infos', {'fields':['email']}),
    ('standard', {'fields':['status']}),
    ]

@admin.register(models.Contact)
class ContactAdmin(Action):
    list_display = ('full_name','date_add','date_update','status')
    list_filter = ('date_add','date_update','status')
    search_fields = ('full_name',)
    date_hierarchy = 'date_add'
    list_display_links = ['full_name']
    fieldsets = [
    ('Contact_infos', {'fields':['full_name','email','subjects','message']}),
    ('standard', {'fields':['status']}),
    ]


@admin.register(models.Contact_info)
class Contact_infoAdmin(Action):
    list_display = ('address','date_add','date_update','status')
    list_filter = ('date_add','date_update','status')
    search_fields = ('address',)
    date_hierarchy = 'date_add'
    list_display_links = ['address']
    fieldsets = [
    ('Contact_info_infos', {'fields':['address','phone','emailAdress']}),
    ('standard', {'fields':['status']}),
    ]


@admin.register(models.About)
class AboutAdmin(Action):
    list_display = ('titre','image_view','date_add','date_update','status')
    list_filter = ('date_add','date_update','status')
    search_fields = ('titre',)
    date_hierarchy = 'date_add'
    list_display_links = ['titre']
    fieldsets = [
    ('About_infos', {'fields':['titre','description','lien','image']}),
    ('standard', {'fields':['status']}),
    ]
    def image_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.image.url))
        



@admin.register(models.Our_team)
class Our_teamAdmin(Action):
    list_display = ('nom','image_view','date_add','date_update','status')
    list_filter = ('date_add','date_update','status')
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    fieldsets = [
    ('Our_team_infos', {'fields':['image','nom','description','fonction']}),
    ('standard', {'fields':['status']}),
    ]
    def image_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.image.url))
            
