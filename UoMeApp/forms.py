from django import forms
from models import UoMePost

class UoMePostForm(forms.ModelForm):
    
    class Meta:
        model = UoMePost
        fields = ('ower_name', 'receiver_name', 'event', 'item_name', 'price', 'comments')