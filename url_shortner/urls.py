from django.contrib import admin
from django.urls import path, include
from post import urls
from users import urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('post.urls')),
    path('',include('users.urls')),


]