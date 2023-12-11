from django.urls import path
from .views import map_view

urlpatterns = [
    path('map/<int:map_id>/', map_view, name='map_detail'),
    path('maps/<pgm_file>/', map_view, name='serve_pgm_file'),
]