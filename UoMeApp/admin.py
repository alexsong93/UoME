import models
from django.contrib import admin
from django.contrib.auth.models import User, Group

class GroupAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)} 
   
class UoMePostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("item_name",)}

    def save_model(self, request, obj, form, change):
        if not change:
            obj.group = request.group
        obj.save()
        
class UserProfileAdmin(admin.ModelAdmin):
    prepopulated_fields = {}

admin.site.register(models.Group, GroupAdmin)       
admin.site.register(models.UoMePost, UoMePostAdmin)
admin.site.register(models.UserProfile, UserProfileAdmin)
