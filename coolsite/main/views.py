from django.shortcuts import render, HttpResponse

from main.models import SideBar, Blogs


def index(request):

    context={
        'key':'Главная',
    }
    return render(request, 'main/index.html', context=context)

def show_blog(request):
    blogs=Blogs.objects.all()
    return render(request, 'main/main_blogs.html', {'blogs':blogs})


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