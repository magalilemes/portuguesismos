from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

class ClasseGramatical(models.Model):
    """Modelo representando uma classe gramatical."""
    nome = models.CharField(max_length=20)

    class Meta:
        ordering = ['nome']
        verbose_name_plural = 'classes gramaticais'

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('categoria-detail', kwargs={"slug": self.slug})

class Termo(models.Model):
    """Modelo representando um termo estrangeiro."""
    termo = models.CharField(max_length=200)
    traducao = models.CharField(max_length=200)
    definicao = models.TextField(help_text='Insira uma definição em português do termo.')
    classe_gramatical = models.ForeignKey(ClasseGramatical, on_delete=models.SET_NULL, null=True)
    categoria = models.ManyToManyField(Categoria)
    grafia_aportuguesada = models.CharField(max_length=200, null=True, blank=True)
    equivalencia = models.IntegerField(null=True, blank=True, validators=[
        MinValueValidator(1),
        MaxValueValidator(3)])

    class Meta:
        ordering = ['termo']

    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.termo

    def get_absolute_url(self):
        return reverse("termo-detail", kwargs={"slug": self.slug})
