from django.shortcuts import render, get_object_or_404
from django.http import FileResponse
from django.conf import settings
import os
from .models import Map

def map_view(request, map_id, pgm_file=None):
    map_instance = get_object_or_404(Map, pk=map_id)
    
    if pgm_file:
        pgm_path = os.path.join(settings.BASE_DIR, 'maps', pgm_file)
        return FileResponse(open(pgm_path, 'rb'), content_type='image/png')

    return render(request, 'map/map_detail.html', {'map': map_instance})
