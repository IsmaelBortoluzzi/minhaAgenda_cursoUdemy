from django.urls import path
from . import views

urlpatterns = [
    path('', views.contatos, name='contatos')
]
