from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.views.generic import ListView, View
from entries.models import Entry, Folder


class HomePage(LoginRequiredMixin, ListView):
    template_name = 'home.html'
    model = Folder
    context_object_name = 'folders'

    def get_queryset(self):
        """Eventually, this will be limited by permissions."""
        return Folder.objects.filter(parent=None)


class EntryListAjax(LoginRequiredMixin, View):
    """Ajax view to display list of entries in the folder specified by PK."""

    def get(self, request, pk):
        entries = Folder.objects.get(id=pk).entries.all()
        data = dict()
        context = {'entries': entries}
        data['entry_list'] = render_to_string('ajax/entry_list.html',
                                              context,
                                              request=request)
        return JsonResponse(data)


class EntryDetailAjax(LoginRequiredMixin, View):
    def get(self, request, pk):
        entry = get_object_or_404(Entry, pk=pk)
        data = dict()
        context = {'entry': entry}
        data['entry'] = render_to_string('ajax/entry_modal.html',
                                         context,
                                         request=request)
        return JsonResponse(data)
