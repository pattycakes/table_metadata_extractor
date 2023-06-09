from django.urls import path
from .views import get_table_metadata

urlpatterns = [
    path('', get_table_metadata, name='get_table_metadata'),
]
