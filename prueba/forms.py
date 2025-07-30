from django import forms
from .models import Website, User

class WebsiteForm(forms.ModelForm):
    class Meta:
        model = Website
        fields = ['name', 'url', 'release_date', 'rating', 'status','user', 'owner']
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']