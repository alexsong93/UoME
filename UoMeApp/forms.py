from django import forms
from models import UoMePost, Group

class UoMePostForm(forms.ModelForm):
    
    class Meta:
        model = UoMePost
        fields = ('group','ower_name', 'receiver_name', 'event', 'item_name', 'price', 'comments')
        
class CreateGroupForm(forms.ModelForm):
    
    class Meta:
        model = Group
        fields = ('name','members','description')