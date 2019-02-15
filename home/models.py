from django.db import models

# Create your models here.
class Home(models.Model):
    kategori_resto = models.CharField(max_length = 255)
    images = models.CharField(max_length = 255)
    deskripsi = models.CharField(max_length = 255)

    def __str__(self):
        return self.kategori_resto

class Kategori(models.Model):
    nama_resto = models.CharField(max_length = 255)
    images = models.CharField(max_length = 255)
    alamat = models.CharField(max_length = 255)
    gaya = models.CharField(max_length = 255)
    # kategori = models.CharField(max_length = 255)
    kategori_id = models.ForeignKey(Home, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.nama_resto