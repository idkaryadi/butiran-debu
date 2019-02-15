from django.db import models
from django.db.models import CharField
from django.db.models import TextField
from django.utils import timezone

# Create your models here.

class Reserv(models.Model):
    Nama = models.CharField(max_length=100, default='')
    Email = models.CharField(max_length=100, default='')
    Kata_sandi = models.CharField(max_length=100, default='')
    Tanggal = models.DateTimeField(default=timezone.now)
    Jumlah = models.CharField(max_length=100, default='')
    DP = models.CharField(max_length=100, default='')
    Metode_Pembayaran = models.CharField(max_length=100, default='')
    Pesanan = models.CharField(max_length=1000, default='')

    def __str__(self):
        return self.Nama

class Review(models.Model):
    Name = models.CharField(max_length=100, default='')
    Email = models.CharField(max_length=100, default='')
    Kata_sandi = models.CharField(max_length=100, default='')
    Tanggal = models.DateTimeField(default=timezone.now)
    Komentar = models.CharField(max_length=1000, default='')

    def __str__(self):
        return self.Name