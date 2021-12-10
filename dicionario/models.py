from django.db import models
from django.urls import reverse

class ClasseGramatical(models.Model):
    """Modelo representando uma classe gramatical."""
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Termo(models.Model):
    """Modelo representando um termo estrangeiro."""
    termo = models.CharField(max_length=200)
    traducao = models.CharField(max_length=200)
    definicao = models.TextField(help_text='Insira uma definição em português do termo.')
    classe_gramatical = models.ForeignKey(ClasseGramatical, on_delete=models.SET_NULL, null=True)
    categoria = models.CharField(max_length=100)
    equivalencia = models.IntegerField()

    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.termo

    def get_absolute_url(self):
        return reverse("termo_detail", kwargs={"slug": self.slug})
