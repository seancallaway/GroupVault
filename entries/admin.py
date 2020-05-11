from django.contrib import admin
from entries.forms import EntryAdminAddForm, EntryAdminChangeForm
from entries.models import Entry, Folder


class EntryAdmin(admin.ModelAdmin):
    model = Entry
    list_display = ['name', 'folder', ]
    list_filter = ('folder__name', )

    def get_form(self, request, obj=None, change=False, **kwargs):
        if change:
            kwargs['form'] = EntryAdminChangeForm
        else:
            kwargs['form'] = EntryAdminAddForm
        return super().get_form(request, obj, change, **kwargs)


class FolderAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'parent',
    ]


admin.site.register(Entry, EntryAdmin)
admin.site.register(Folder, FolderAdmin)
