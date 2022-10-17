from django.urls import path
from .views import *

urlpatterns = [
    path('', read, name = 'read'),
    path('create/', create, name = 'create'),
    path('update/', update, name='update'),
    path('delete/', delete, name = 'delete')
]