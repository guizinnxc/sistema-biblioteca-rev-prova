from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import livros
from .serializers import LivrosSerializer

@api_view(['GET'])
def listar_livros(request):
    livros_list = livros.objects.all()
    serializer = LivrosSerializer(livros_list, many=True)
    return Response(serializer.data)