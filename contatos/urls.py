from django.urls import path
from . import views

urlpatterns = [
    path('', views.contatos, name='contatos'),
    path('<int:contato_id>', views.ver_contato, name='ver_contato'),
]
