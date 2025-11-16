from django.contrib import admin
from .models import Despesa

@admin.register(Despesa)
class DespesaAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'categoria', 'valor', 'data')
    list_filter = ('categoria', 'data')
    search_fields = ('descricao',)
