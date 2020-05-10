from django.urls import path
from entries.views import HomePage, EntryDetailAjax, EntryListAjax

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('ajax/folder/<int:pk>', EntryListAjax.as_view(), name='ajax-folder'),
    path('ajax/entry/<int:pk>', EntryDetailAjax.as_view(), name='ajax-entry'),
]
