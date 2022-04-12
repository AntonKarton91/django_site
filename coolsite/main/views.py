from django.shortcuts import render, HttpResponse
# from models import SideBar
from main.models import SideBar


def index(request):
    side_bar=SideBar.objects.all()
    context={
        'key':'Главная',
        'side_bar':side_bar,
    }


    return render(request, 'main/index.html', context=context)

def index_dko(request):
    context={
        'key':'ДКО'
    }
    return render(request, 'main/index.html', context=context)


def index_prodaji(request):
    context={
        'key':'Отдел продаж'
    }
    return render(request, 'main/index.html', context=context)


def index_snab(request):
    context={
        'key':'Отдел снабжения'
    }
    return render(request, 'main/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponse('Страница не найдена')