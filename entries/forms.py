from django import forms
from entries.models import Entry


class EntryAdminChangeForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = (
            'name',
            'folder',
            'url',
            'login',
            'description',
        )


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
