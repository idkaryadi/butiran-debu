from django.db import models

# Create your models here.
class Kategori(models.Model):
    nama_resto = models.CharField(max_length = 255)
    images = models.CharField(max_length = 255)
    alamat = models.CharField(max_length = 255)
    gaya = models.CharField(max_length = 255)
    kategori = models.CharField(max_length = 255)

    def __str__(self):
        return self.nama_resto