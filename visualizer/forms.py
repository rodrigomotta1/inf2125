from django import forms
from visualizer.models import UserProfile

class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['notifications_enabled']
        widgets = {
            'notifications_enabled': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }