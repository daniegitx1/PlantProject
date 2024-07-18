# plants/urls.py

from django.urls import path
from .views import view_names_edit

urlpatterns = [
    # Other URL patterns if you have additional views
    path('plants/edit-names/', view_names_edit, name='edit-names'),
]




