from django.urls import path
from .views import listar_emprestimos 
urlpatterns = [
path('emprestimos/', listar_emprestimos),
]