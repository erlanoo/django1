from django import forms
from . import models


class TVShowForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = "__all__"