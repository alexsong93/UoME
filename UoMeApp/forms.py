from django import forms
from models import UoMePost, Group
from django.contrib.auth.models import User

class UoMePostForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        group_id = kwargs.pop('group_id')
        user = kwargs.pop('user')
        super(UoMePostForm, self).__init__(*args, **kwargs)
        group_members = Group.objects.get(id=group_id).members
        self.fields['group'].queryset = Group.objects.filter(id=group_id)
        self.fields['group'].initial = Group.objects.get(id=group_id)
        self.fields['ower_name'].queryset = group_members
        self.fields['receiver_name'].queryset = group_members
        self.fields['receiver_name'].initial = user
    
    class Meta:
        model = UoMePost
        fields = ('group','ower_name', 'receiver_name', 'event', 'item_name', 'price', 'comments')
        
class CreateGroupForm(forms.ModelForm):
    
    class Meta:
        model = Group
        fields = ('name','members','description')