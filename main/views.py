from django.shortcuts import render


# Create your views here.

def auth(request):
    context = {'lol': 'TEST',}
    return render(request, 'auth/auth.html', context)


def register(request):
    context = {'lol': 'TEST',}
    return render(request, 'register/register.html', context)
