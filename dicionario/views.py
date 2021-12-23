from django.views import generic
from .models import Categoria, Termo
from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import get_object_or_404

def Home(request):
    return render(request, 'index.html')

class TermoDetailView(generic.DetailView):
    model = Termo
    template_name = 'termo_detail.html'

class BuscaView(generic.ListView):
    model = Termo
    template_name = 'busca.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Termo.objects.filter(Q(termo__icontains=query))

        return object_list

class CategoriaView(generic.ListView):
    model = Categoria
    template_name = 'categoria.html'

class CategoriaDetailView(generic.DetailView):
    model = Categoria
    template_name = 'categoria_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['termos'] = Termo.objects.filter(categoria=self.object).order_by('termo')
        return context
