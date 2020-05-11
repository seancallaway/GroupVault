from django import forms
from entries.models import Entry


class EntryAdminAddForm(forms.ModelForm):
    secret = forms.CharField(max_length=512)

    def save(self, commit=True):
        entry_instance = super(EntryAdminAddForm, self).save(commit=False)
        entry_instance.secret = self.cleaned_data['secret']
        entry_instance.save()
        return entry_instance

    class Meta:
        model = Entry
        fields = (
            'name',
            'folder',
            'url',
            'login',
            'secret',
            'description',
        )


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
