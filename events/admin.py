from django.contrib import admin
from django.utils.safestring import mark_safe
# Register your models here.
from . import models
from actions.actions import Action

@admin.register(models.Event)
class EventAdmin(Action):
    list_display = ('image_view','titre','date_add','date_update','status')
    list_filter = ('date_add','date_update','status')
    search_fields = ('titre',)
    date_hierarchy = 'date_add'
    list_display_links = ['titre']
    fieldsets = [
    ('Event_infos', {'fields':['image','titre','date']}),
    ('standard', {'fields':['status']}),
    ]

    def image_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.image.url))
