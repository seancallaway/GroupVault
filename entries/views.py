from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from entries.models import Folder


class HomePage(LoginRequiredMixin, ListView):
    template_name = 'home.html'
    model = Folder
    context_object_name = 'folders'

    def get_queryset(self):
        """Eventually, this will be limited by permissions."""
        return Folder.objects.filter(parent=None)
