from django.db import models

class Selo_Fonografico(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome

class Artista(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome
# Create your models here.
class Disco(models.Model):
    nome = models.CharField(max_length=150, verbose_name="Título do Disco")
    descricao = models.TextField(max_length=600, verbose_name="Descrição")
    ano = models.IntegerField()
    pais = models.CharField(max_length=150)
    genero = models.CharField(max_length=150, verbose_name="Gênero Musical")
    quantidade = models.IntegerField(verbose_name="Quantidade de Cópias")
    selo_fonografico = models.ForeignKey(Selo_Fonografico, on_delete=models.CASCADE, verbose_name="Gravadora")
    artistas = models.ManyToManyField(Artista)
    preco = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Preço")

    def __str__(self):
        return self.nome