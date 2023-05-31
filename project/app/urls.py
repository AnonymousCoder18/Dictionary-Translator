from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('index', views.index, name="index"),
    path('register', views.register, name="register"),
    path('LogOut', views.LogOut, name="LogOut"),
    
    path('meaning', views.meaning, name="meaning"),
    path('translate', views.translate, name="translate"),
]