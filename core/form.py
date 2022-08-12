
from django.contrib.auth.models import User
from django import forms


class SiginInForms(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']
