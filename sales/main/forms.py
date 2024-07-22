from django import forms
from .models import *

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'description', 'price']
        widgets = {
            'title': forms.TextInput(),
            'description': forms.Textarea(),
            'price': forms.NumberInput(),
        }