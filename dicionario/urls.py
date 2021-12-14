from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('busca/', views.BuscaView.as_view(), name='busca'),
    path('dicionario/<slug:slug>', views.TermoDetailView.as_view(), name="termo-detail"),
]
