from django.shortcuts import render,redirect
from django.views.generic.edit import FormView
#from django.views.generic import TemplateView
#from django.views.generic.base import View
#from django.contrib.auth import login
from .forms import RegisterFormUser
#from main.models import Person
from django.http import HttpResponseRedirect
#from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def auth(request):
    context = {'lol': 'TEST',}
    return render(request, 'auth/auth.html', context)


def register(request):
    if request.method == 'POST':
        form = RegisterFormUser(request.POST)
        if form.is_valid():
            form.save()
        return redirect('auth/auth.html')
    else:
        form = RegisterFormUser()
        return render(request, 'register/register.html', {'form': form})




