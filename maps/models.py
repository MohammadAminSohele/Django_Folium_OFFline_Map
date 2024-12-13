from django.db import models

# Create your models here.

class MBTiles(models.Model):
    file = models.FileField(upload_to='mbtiles/')

    def __str__(self):
        return self.file.name