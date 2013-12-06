import models
from django.contrib import admin
from django.contrib.auth.models import User, Group

class GroupAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)} 
    
#     def has_change_permission(self, request, obj=None):
#         has_class_permission = super(GroupAdmin, self).has_change_permission(request, obj);
#         if not has_class_permission:
#             return False
#         if obj is not None and not request.user.is_superuser and request.user.id != obj.auth:
#             return False
#         return True
#     
#     def queryset(self, request):
#         if request.user.is_superuser:
#             return Group.objects.all()
#         return Group.objects.filter(author=request.user)
#     
#     def save_model(self, request, obj, form, change):
#         if not change:
#             obj.author = request.user
#         obj.save()

class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
   
class UoMePostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("item_name",)}


admin.site.register(models.Group, GroupAdmin)
admin.site.register(models.Event, EventAdmin)         
admin.site.register(models.UoMePost, UoMePostAdmin)
