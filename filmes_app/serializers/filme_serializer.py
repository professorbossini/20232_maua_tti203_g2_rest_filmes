from rest_framework  import serializers
from .genero_serializer import GeneroSerializer
from filmes_app.models import Filme
class FilmeSerializer(serializers.ModelSerializer):
  genero = GeneroSerializer()
  class Meta:
    model = Filme
    fields = '__all__'