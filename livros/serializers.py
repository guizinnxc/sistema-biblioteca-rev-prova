from rest_framework import serializers
from .models import livros 
class LivrosSerializer(serializers.ModelSerializer):
 class Meta:
  model = livros
  fields = ['id', 'nome', 'tipo']