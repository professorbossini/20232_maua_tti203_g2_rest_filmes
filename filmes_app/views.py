from django.shortcuts import render
from rest_framework import generics
from .models import Filme
from .serializers import FilmeSerializer
# Create your views here.
#POST /filmes {titulo..., descricao...}
#1. dizer qual é a tabela envolvida
#2. como se dá a serialização desse objeto
#GET /filmes
#1. dizer qual é a tabela envolvida
#2. como se dá a serialização de cada objeto
class FilmeListCreate(generics.ListCreateAPIView):
  queryset = Filme.objects.all()
  serializer_class = FilmeSerializer