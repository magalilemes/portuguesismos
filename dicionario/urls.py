from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>', views.TermoDetailView.as_view(), name="termo-detail"),
]
