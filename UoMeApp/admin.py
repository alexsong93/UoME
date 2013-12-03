import models
from django.contrib import admin
from django.contrib.auth.models import User

class GroupAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)} 

class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
   
class UoMePostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("item_name",)}


admin.site.register(models.Group, GroupAdmin)
admin.site.register(models.Event, EventAdmin)         
admin.site.register(models.UoMePost, UoMePostAdmin)
