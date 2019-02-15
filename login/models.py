from django.db import models

# Create your models here.
class Login(models.Model):
    nama_akun = models.CharField(max_length = 255)
    password = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.judul