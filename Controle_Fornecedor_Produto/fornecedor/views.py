from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Fornecedor, Contato
from django.forms import inlineformset_factory
from django.core.paginator import Paginator
from .forms import ForncedorForm, ContatoForm


def fornecedores(request):
    fornecedor_list = Fornecedor.objects.all()
    paginator = Paginator(fornecedor_list, 10)
    page = request.GET.get('page')
    fornecedores = paginator.get_page(page)
    return render(request, 'fornecedor/list_fornecedor.html', {'fornecedores': fornecedores})


def novoFornecedor(request):
    if request.method == "GET":
       form = ForncedorForm
       form_contato_factory = inlineformset_factory(Fornecedor, Contato, form=ContatoForm, extra=1)
       formset =form_contato_factory
       context = {
           'form': form,
           'formset': formset,
       }
       return render(request, 'fornecedor/create_fornecedor.html', context)
    elif request.method == "POST":
        form = ForncedorForm(request.POST)
        form_contato_factory = inlineformset_factory(Fornecedor, Contato, form=ContatoForm)
        formset = form_contato_factory(request.POST)
        if form.is_valid() and formset.is_valid():
            fornecedor = form.save()
            formset.instance = fornecedor
            formset.save()
            return redirect('listar_fornecedor')
        else:
            context = {
                'form': form,
                'formset': formset,
            }
            return render(request, 'fornecedor/create_fornecedor.html', context)


def fornecedorEditar(request, id):
    if request.method == "GET":
        objeto = Fornecedor.objects.filter(id=id).first()
        if objeto is None:
            return redirect('listar_fornecedor')
        form = ForncedorForm(instance=objeto)
        form_contato_factory = inlineformset_factory(Fornecedor, Contato, form=ContatoForm, extra=0)
        formset = form_contato_factory(instance=objeto)
        context = {
           'form': form,
           'formset': formset,
        }
        return render(request, 'fornecedor/edite_fornecedor.html', context)
    elif request.method == "POST":
        objeto = Fornecedor.objects.filter(id=id).first()
        if objeto is None:
            return redirect(reverse('listar_fornecedor'))
        form = ForncedorForm(request.POST, instance=objeto)
        form_contato_factory = inlineformset_factory(Fornecedor, Contato, form=ContatoForm, extra=0)
        formset = form_contato_factory(request.POST, instance=objeto)
        if form.is_valid() and formset.is_valid():
            fornecedor = form.save()
            formset.instance = fornecedor
            formset.save()
            return redirect('listar_fornecedor')
        else:
            context = {
             'form': form,
              'formset': formset,
             }
            return render(request, 'fornecedor/create_fornecedor.html', context)

def fornecedorVer(request, id):
    fornecedor = Fornecedor.objects.get(id=id)
    return render(request, 'fornecedor/detalhes_fornecedor.html', {'fornecedor':fornecedor})



def fornecedorDetete(request, id):
    fornecedor = Fornecedor.objects.get(id=id)
    if request.method == "POST":
        fornecedor.delete()
        return redirect('listar_fornecedor')
    else:
        return render(request, 'fornecedor/delete_confirme.html', {'fornecedor': fornecedor})



