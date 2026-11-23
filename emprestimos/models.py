from django.db import models
from livros.models import livros
from leitores.models import leitores
class emprestimos(models.Model):
 STATUS_CHOICES = [
  ('ABERTO','Aberto'),
  ('DEVOLVIDO','Devolvido'),
]
 descricao = models.CharField(max_length=200)
 valor = models.DecimalField(max_digits=10,
decimal_places=2)
 data = models.DateField()
 tipo = models.CharField(max_length=10,
choices=STATUS_CHOICES, default='ABERTO')
 leitores = models.ForeignKey(leitores,
on_delete=models.CASCADE)
 livros = models.ForeignKey(livros,
on_delete=models.CASCADE)
 def __str__(self):
  return f"{self.descricao} - {self.valor}"