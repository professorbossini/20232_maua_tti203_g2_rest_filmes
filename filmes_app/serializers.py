from rest_framework  import serializers
from .models import Filme
class FilmeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Filme
    fields = '__all__'
# {titulo: fewalçk, descricao: } => Filme
#Filme => {titulo}
#{
#   titulo fewlajl,
#   descricao: fewkçlafjw,
#   diretor: kfejwçalfw,
#   genero: 1
# }

# {
#   titulo fewlajl,
#   descricao: fewkçlafjw,
#   diretor: kfejwçalfw,
#   genero: {
#     id: 1,
#     descricao: fçjewla
#   }
# }


