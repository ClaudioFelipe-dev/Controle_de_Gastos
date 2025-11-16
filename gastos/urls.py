from django.urls import path
from . import views

app_name = 'gastos'

urlpatterns = [
    path('', views.lista_despesas, name='lista_despesas'),
    path('nova/', views.nova_despesa, name='nova_despesa'),
    path('editar/<int:id>/', views.editar_despesa, name='editar_despesa'),
    path('excluir/<int:id>/', views.excluir_despesa, name='excluir_despesa'),
]
