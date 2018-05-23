from django import forms
from mini_app.models import archery_boards


class archery_boards_form(forms.ModelForm):
    class Meta():
        model = archery_boards
        fields = ('name',)
