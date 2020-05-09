from django.contrib import admin
from entries.models import Folder


class FolderAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'parent',
    ]


admin.site.register(Folder, FolderAdmin)
