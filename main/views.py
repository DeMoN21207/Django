from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
# from django.views.generic import TemplateView
# from django.views.generic.base import View
# from django.contrib.auth import login
from .forms import RegisterFormUser
# from main.models import Person
from django.http import HttpResponseRedirect
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def auth(request):
    context = {'lol': 'TEST', }
    return render(request, 'auth/auth.html', context)





def register_done(request):
    return render(request, 'register/register_done.html')


class register1(FormView):
    form_class = RegisterFormUser
    success_url = 'auth'
    template_name='register/register.html'
    def form_valid(self, form):
        form.save()
        return super(register1, self).form_valid(form)

    def form_invalid(self, form):
        return super(register1, self).form_invalid(form)
