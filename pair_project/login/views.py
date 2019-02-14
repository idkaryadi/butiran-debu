from django.shortcuts import render, redirect
from .models import Login
from .forms import LoginForm

# Create your views here.
def input_post(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(blog) #ke home
    
    else:
        form = LoginForm()
    return render(request, ) #ke blog