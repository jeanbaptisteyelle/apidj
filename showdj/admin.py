from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe
from actions.actions import Action
# Register your models here. 
@admin.register(models.Show)
class ShowAdmin(Action):
    list_display = ('titre','date_add','date_update','status','image_view')
    list_filter = ('date_add','date_update','status')
    search_fields = ('titre',)
    date_hierarchy = 'date_add'
    list_display_links = ['titre']
    fieldsets = [
    ('Show_infos', {'fields':['titre','description','created_by','image','musique']}),
    ('standard', {'fields':['status']}),
    ]

    def image_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.image.url))


