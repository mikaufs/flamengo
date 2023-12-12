from django.shortcuts import render, reverse, HttpResponseRedirect
from .models import Disco, Artista
from django.db import models
from .forms import DiscoForm
from django.core.paginator import Paginator
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required


@login_required(login_url="accounts/login")
def dashboard(request):
    total_discos = Disco.objects.count()
    total_artistas = Artista.objects.count()
    total_copias = Disco.objects.aggregate(
        total_copias=models.Sum('quantidade'))
    resultado = total_copias['total_copias']
    context = {
        'total_discos': total_discos,
        'total_artistas': total_artistas,
        'total_copias': resultado,
    }
    return render(request, "disco/dashboard.html", context)


@login_required(login_url="accounts/login")
def index(request):
    user = authenticate(request=request)
    artistas = Artista.objects.all()
    discos = Disco.objects.all()

    nome_disco = request.GET.get('nome')
    nome_artista = request.GET.get('artista')
    pagina = request.GET.get('pagina')

    if (nome_artista != None and nome_artista != ''):
        discos = discos.filter(artistas__nome__icontains=nome_artista)
    if (nome_disco != None and nome_disco != ''):
        discos = discos.filter(nome__icontains=nome_disco)

    paginator = Paginator(discos, 10)

    if (pagina != None and pagina != ''):
        page_obj = paginator.page(pagina)
        pagina_atual = pagina
    else:
        page_obj = paginator.page(1)
        pagina_atual = 1

    num_pages = paginator.num_pages
    lista_paginas = []
    for i in range(0, num_pages):
        lista_paginas.append(i + 1)

    context = {'discos': page_obj, 'artistas': artistas,
               'lista_paginas': lista_paginas, 'pagina_atual': pagina_atual,
               'has_next': page_obj.has_next(), 'proxima_pagina': int(pagina_atual) + 1,
               'pagina_anterior': int(pagina_atual) - 1, 'username': request.user.username}
    return render(request, "disco/discos.html", context)


@login_required(login_url="accounts/login")
def create_disco(request):
    context = {'acao': 'Cadastrar'}
    if request.POST:
        form = DiscoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            context['form'] = form
            return render(request, "disco/form.html", context)
    else:
        context['form'] = DiscoForm()

        return render(request, "disco/form.html", context)


@login_required(login_url="accounts/login")
def edit_disco(request, pk):
    context = {'acao': 'Editar'}
    if request.POST:
        form = DiscoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            context['form'] = form
            return render(request, "disco/form.html", context)
    else:
        disco = Disco.objects.get(pk=pk)
        form = DiscoForm(instance=disco)
        context['form'] = form

        return render(request, "disco/form.html", context)


@login_required(login_url="accounts/login")
def delete_disco(request, pk):
    disco = Disco.objects.get(pk=pk)
    disco.delete()
    return HttpResponseRedirect(reverse('index'))


def login_view(request):
    if(request.method == 'GET'):
        return render(request, "disco/accounts/login.html")
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is None:
            return HttpResponseRedirect(reverse('login'))
        login(request, user)
        return HttpResponseRedirect(reverse('index'))




def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
