from django.shortcuts import render, HttpResponse
from django.views.generic import ListView

from .models import SideBar, Blogs

from .forms import RegistrationForm


def index(request):

    context={
        'key':'Главная',
    }
    return render(request, 'main/index.html', context=context)

class ShowBlog(ListView):
    model=Blogs
    template_name = 'main/main_blogs.html'
    context_object_name = 'blogs'


    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        print(context['blogs'][0].content)
        return context





# def show_blog(request):
#     blogs=Blogs.objects.all()
#     return render(request, 'main/main_blogs.html', {'blogs':blogs})


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

def registration(request):

    if request.method=='POST':
        form = RegistrationForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
    else:
        form = RegistrationForm



    context = {
        'key': 'Регистрация',
        'form':form,
    }
    return render(request, 'main/registration.html', context=context)