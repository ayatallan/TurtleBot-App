from django.db import models

# Create your models here.
from django.db import models

class Map(models.Model):
    name = models.CharField(max_length=255)
    yaml_file = models.FileField(upload_to='map_files/')
    pgm_file = models.FileField(upload_to='map_files/')