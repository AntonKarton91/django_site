from django.shortcuts import render, HttpResponse

main_menu=[
    {'title':'Главная', 'url':"home"},
    {'title':'ДКО', 'url':"dko"},
    {'title':'Отдел продаж', 'url':"prodaji"},
    {'title':'Отдел снабжения', 'url':"snab"},
]

def index(request):
    context={
        'main_menu':main_menu,
    }


    return render(request, 'main/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponse('Страница не найдена')