from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, TemplateView, CreateView
from django.views.generic.edit import ProcessFormView

from .utils import *
from .models import *
from .forms import *




class MainDko(DataMixinDko,ListView):
        model = DkoEmployer
        template_name = 'dko/main_dko.html'
        context_object_name = 'dko_emplyers'

        def get_context_data(self, *, object_list=None, **kwargs):

                context=super().get_context_data(**kwargs)
                context.update({'tasks': Tasks.objects.all()})
                c_def= self.get_user_context(title='Задачи ДКО')
                return dict(list(context.items())+list(c_def.items()))

class Registration(DataMixinDko,CreateView):
        model = MarketEmployer
        form_class = AddEmployer
        template_name = 'dko/create_user.html'
        success_url = reverse_lazy('main_dko')

        def get_context_data(self, *, object_list=None, **kwargs):
                context = super().get_context_data(**kwargs)
                c_def = self.get_user_context(title='Регистрация')
                return dict(list(context.items()) + list(c_def.items()))

        def form_valid(self, form):
                form.instance.initials = ((self.request.POST['name'])[0]).upper()

                return super().form_valid(form)

        # def post(self, request, *args, **kwargs):
        #         print(request.POST)
        #         form = self.get_form()
        #         print(form.name)
        #         if form.is_valid():
        #                 return self.form_valid(form)
        #         else:
        #                 return self.form_invalid(form)

class ShowEquipment(ListView):
        model = Equipment
        template_name = 'dko/show_eq.html'
        context_object_name = 'equipments_list'

        def get_queryset(self):
                return Equipment.objects.filter(client__slug=self.kwargs['client_slug'])
        def get_context_data(self, *, object_list=None, **kwargs):
                context=super().get_context_data(**kwargs)
                context.update({'mod2':Client.objects.all()})
                context['main_menu']=main_menu
                context['title']='Изделия'
                context['side_bar'] = side_bar
                return context


