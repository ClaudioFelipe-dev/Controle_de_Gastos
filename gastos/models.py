from django.db import models

class Despesa(models.Model):
    CATEGORIAS = [
        ('Alimentação', 'Alimentação'),
        ('Transporte', 'Transporte'),
        ('Lazer', 'Lazer'),
        ('Saúde', 'Saúde'),
        ('Outros', 'Outros'),
    ]

    descricao = models.CharField(max_length=200)
    categoria = models.CharField(max_length=50, choices=CATEGORIAS, default='Outros')
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.descricao} — R$ {self.valor}"
