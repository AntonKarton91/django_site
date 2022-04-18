from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, TemplateView

from .models import *
main_menu = [
        {'title': 'Главная', 'url': "home"},
        {'title': 'ДКО', 'url': "dko"},
        {'title': 'Отдел продаж', 'url': "prodaji"},
        {'title': 'Отдел снабжения', 'url': "snab"},
        {'title': 'Регистрация', 'url': "registration"},
    ]

side_bar = [
        {'title': 'Задачи ДКО', 'url': "dko_tasks"},
        {'title': 'Изделия', 'url': "production"},
        {'title': 'other', 'url': "other"},

    ]

class MainDko(TemplateView):
        template_name = 'dko/main_dko.html'
        def get_context_data(self, *, object_list=None, **kwargs):
                context=super().get_context_data(**kwargs)
                context['main_menu']=main_menu
                context['side_bar']=side_bar
                context['title']='Задачи ДКО'
                return context


class ShowEquipment(ListView):
        model = Equipment
        template_name = 'dko/show_eq.html'
        context_object_name = 'equipments_list'

        def get_queryset(self):
                return Equipment.objects.filter(client__slug=self.kwargs['client_slug'])
        def get_context_data(self, *, object_list=None, **kwargs):
                context=super().get_context_data(**kwargs)
                context['main_menu']=main_menu
                context['title']='Изделия'
                context['side_bar'] = side_bar
                return context


