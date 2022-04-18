from django.shortcuts import render
from django.views.generic import ListView

from .models import *
main_menu = [
        {'title': 'Главная', 'url': "home"},
        {'title': 'ДКО', 'url': "dko"},
        {'title': 'Отдел продаж', 'url': "prodaji"},
        {'title': 'Отдел снабжения', 'url': "snab"},
        {'title': 'Регистрация', 'url': "registration"},
    ]

class ShowEquipment(ListView):
        model = Equipment
        template_name = 'dko/show_eq.html'
        context_object_name = 'equipments_list'

        def get_queryset(self):
                return Equipment.objects.filter(client__slug=self.kwargs['client_slug'])
        def get_context_data(self, *, object_list=None, **kwargs):
                context=super().get_context_data(**kwargs)
                context['main_menu']=main_menu
                context['title']='Оборудование'
                return context


