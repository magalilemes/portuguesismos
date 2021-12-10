from django.views import generic
from .models import Termo
from django.shortcuts import get_object_or_404

class TermoDetailView(generic.DetailView):
    model = Termo
    template_name = 'termo_detail.html'

