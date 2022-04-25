main_menu = [
        {'title': 'Главная', 'url': "home"},
        {'title': 'ДКО', 'url': "dko"},
        {'title': 'Отдел продаж', 'url': "prodaji"},
        {'title': 'Отдел снабжения', 'url': "snab"},
        {'title': 'Регистрация', 'url': "registration"},
    ]
dko_side_bar = [
        {'title': 'Задачи ДКО', 'url': "dko_tasks"},
        {'title': 'Изделия', 'url': "production"},
        {'title': 'other', 'url': "other"},

    ]

class DataMixin:
    def get_user_context(self, **kwargs):
        context=kwargs
        context['main_menu']=main_menu
        return context

class DataMixinDko(DataMixin):
    def get_user_context(self, **kwargs):
        context=super().get_user_context()
        context['dko_side_bar']=dko_side_bar
        return context
