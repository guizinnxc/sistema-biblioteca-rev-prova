from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import leitores
from .serializers import LeitoresSerializer

@api_view(['GET'])
def listar_leitores(request):
    lista_leitores = leitores.objects.all()
    serializer = LeitoresSerializer(lista_leitores, many=True) 
    return Response(serializer.data)