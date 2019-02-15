from django.shortcuts import render, redirect
# from .forms import Form
# from .models import resto

# Create your views here.

def detail_resto(request):
    # info = Home.object.all()
    return render(request, 'resto/restorant.html', {})

def detail_menu(request):
    return render(request, 'resto/menu.html', {})

def detail_resev(request):
    # if request.method == 'POST':
    #     form = Form(request.POST, request.FILES)
    #     if form.is_valid():
    #         post = form.save_update
    #         form.save()
    #         return redirect(reservasi)

    # else:
    #     form = Form
        return render(request, 'resto/reservasi.html', {})


def komen_resto(request):
    if request.method == 'POST':
        form = Form(request.POST, request.FILES)
        if form.is_valid():
            post = form.save_update
            form.save()
            return redirect(restorant)

    else:
        form = Form
        return render(request, 'resto/restorant.html', {'form': form})

