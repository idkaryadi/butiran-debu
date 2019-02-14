from django.shortcuts import render #, redirect
from .models import Home, Kategori

# Create your views here.
def home(request):
    home = Home.objects.all()
    return render(request, 'home/home.html', {'homes':home}) # #ntar for data in homes

# def temp(request):
#     return render(request, 'home/temp.html')

def cat_detail(request, post_id):
    kategori = Kategori.objects.filter(kategori_id = post_id)
    home = Home.objects.get(pk = post_id)
    data = Home.objects.all()
    return render(request, 'home/cat_detail.html', {'kategori':kategori, 'home':home, 'data':data})
