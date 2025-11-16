from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Despesa


@login_required
def lista_despesas(request):
    despesas = Despesa.objects.order_by('-data', '-created_at')
    total = sum(d.valor for d in despesas)
    return render(request, 'gastos/lista.html', {
        'despesas': despesas,
        'total': total
    })


@login_required
def nova_despesa(request):
    categorias = Despesa.CATEGORIAS  
    if request.method == 'POST':
        descricao = request.POST.get('descricao', '').strip()
        categoria = request.POST.get('categoria', 'Outros')
        valor = request.POST.get('valor', '0')
        data = request.POST.get('data')

        if descricao and valor and data:
            Despesa.objects.create(
                descricao=descricao,
                categoria=categoria,
                valor=valor,
                data=data
            )
            return redirect('gastos:lista_despesas')

    return render(request, 'gastos/nova.html', {
        'categorias': categorias
    })


@login_required
def editar_despesa(request, id):
    despesa = get_object_or_404(Despesa, id=id)
    categorias = Despesa.CATEGORIAS

    if request.method == 'POST':
        despesa.descricao = request.POST.get('descricao', despesa.descricao)
        despesa.categoria = request.POST.get('categoria', despesa.categoria)
        despesa.valor = request.POST.get('valor', despesa.valor)
        despesa.data = request.POST.get('data', despesa.data)
        despesa.save()
        return redirect('gastos:lista_despesas')

    return render(request, 'gastos/editar.html', {
        'despesa': despesa,
        'categorias': categorias
    })


@login_required
def excluir_despesa(request, id):
    despesa = get_object_or_404(Despesa, id=id)

    if request.method == 'POST':
        despesa.delete()
        return redirect('gastos:lista_despesas')

    return render(request, 'gastos/excluir.html', {
        'despesa': despesa
    })
