from django.contrib import admin

class Action(admin.ModelAdmin):

    actions = ('active','desactive')
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'La selection a été activé avec succès')
    active.short_description = 'activer'
        
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, 'La selection a été desactivé avec succès')
    desactive.short_description = 'desactiver'