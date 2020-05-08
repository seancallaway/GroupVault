from django.urls import path
from entries.views import HomePage

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
]
