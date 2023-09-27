from django.db import models

class Genero(models.Model):
  descricao = models.CharField(max_length=100)
  def __str__(self):
    return self.descricao

# Create your models here.
#Object Relational Mapping
class Filme(models.Model):
  titulo = models.CharField(max_length=100)
  descricao = models.TextField()
  diretor = models.CharField(max_length=100)

  def __str__(self):
    return self.titulo
  
