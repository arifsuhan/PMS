from django.urls import path
from .views import *

urlpatterns = [
    path('', book_list, name = 'book_list'),
    path('create/', book_create, name = 'book_create'),
    path('update/', book_update, name = 'book_update'),
    path('delete/', book_delete, name = 'book_delete')
]