from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.http import HttpResponse, HttpResponseRedirect

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Connecte l'utilisateur immédiatement après l'enregistrement
            return redirect('/')  # Redirige vers une page d'accueil ou autre
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'register/register.html', {'form': form})
# Create your views here.
