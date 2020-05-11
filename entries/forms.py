from django import forms
from entries.models import Entry


class EntryForm(forms.ModelForm):
    secret = forms.CharField(max_length=512)

    class Meta:
        model = Entry
        fields = (
            'name',
            'url',
            'login',
            'description',
        )
