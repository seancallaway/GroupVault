from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.views.generic import ListView, View
from entries.forms import EntryForm
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

    def build_context(self, pk, form=None):
        folder = Folder.objects.get(id=pk)
        entries = folder.entries.all()
        if not form:
            form = EntryForm()
        return {
            'folder': folder,
            'form': form,
            'entries': entries,
        }

    def get(self, request, pk):
        data = dict()
        context = self.build_context(pk)
        data['entry_list'] = render_to_string('ajax/entry_list.html',
                                              context,
                                              request=request)
        return JsonResponse(data)

    def post(self, request, pk):
        if request.is_ajax:
            data = dict()

            form = EntryForm(request.POST)
            context = self.build_context(pk, form)
            if form.is_valid():
                Entry.objects.create(
                    name=form.cleaned_data.get('name'),
                    folder=context['folder'],
                    url=form.cleaned_data.get('url', None),
                    login=form.cleaned_data.get('login', None),
                    description=form.cleaned_data.get('description', None),
                    secret=form.cleaned_data.get('secret')
                )
                data['form_is_valid'] = True
                data['folder_id'] = pk
            else:
                data['form_is_valid'] = False
                data['html_form'] = render_to_string('ajax/new_entry_form.html',
                                                     context,
                                                     request=request)
            return JsonResponse(data)

        # non-Ajax request submitted
        return JsonResponse({'error': ''}, status=400)


class EntryDetailAjax(LoginRequiredMixin, View):
    def get(self, request, pk):
        entry = get_object_or_404(Entry, pk=pk)
        data = dict()
        context = {'entry': entry}
        data['entry'] = render_to_string('ajax/entry_modal.html',
                                         context,
                                         request=request)
        return JsonResponse(data)
