from textwrap import shorten
from django.urls import path
from .views import home, redirection

urlpatterns=[
    path('anv3sh',home,name="home"),
    path('anv3sh/<slug:slug>',redirection,name='shorten')
]