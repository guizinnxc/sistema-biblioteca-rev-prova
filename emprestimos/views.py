from django.http import JsonResponse
from .models import emprestimos
def listar_emprestimos(request):
 emprestimos = emprestimos.objects.all().values('id'
,
'nome'
,
'email'
,
'data_cadastro')
 return JsonResponse(list(emprestimos), safe=False)