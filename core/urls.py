

from django.urls import path
from api.views import index, get_data
from django.contrib import admin


urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('get_data/', get_data),
]
