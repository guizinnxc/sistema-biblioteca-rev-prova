from django.urls import path
from .views import listar_leitores
urlpatterns = [
path('leitores/', listar_leitores),
]