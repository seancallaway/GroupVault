from django.contrib import admin
from entries.forms import EntryAdminChangeForm
from entries.models import Entry, Folder


class EntryAdmin(admin.ModelAdmin):
    form = EntryAdminChangeForm
    model = Entry
    list_display = ['name', 'folder', ]


class FolderAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'parent',
    ]


admin.site.register(Entry, EntryAdmin)
admin.site.register(Folder, FolderAdmin)
