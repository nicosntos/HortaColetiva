from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('canteiros/', views.canteiros, name='canteiros'),
    path('mutiroes/', views.mutiroes, name='mutiroes'),
    path('producao/', views.producao, name='producao'),
    path('relatorios/', views.relatorios, name='relatorios'),
]
