from django.conf.urls import url, include
from django.urls import path
from .import views

urlpatterns = [
    path('auth/',views.auth),
    path('register',views.register1.as_view()),
    path('register/register_done',views.register_done),

]