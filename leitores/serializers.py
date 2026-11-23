from rest_framework import serializers
from .models import leitores

class LeitoresSerializer(serializers.ModelSerializer):
  class Meta:
   model = leitores
   fields = ['id', 'nome', 'email', 'data_cadastro']