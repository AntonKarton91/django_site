from django import template
from main.models import SideBar
register=template.Library()

# @register.simple_tag(name='main_menu')
# def get_menu():
#     main_menu=[
#     {'title':'Главная', 'url':"home"},
#     {'title':'ДКО', 'url':"dko"},
#     {'title':'Отдел продаж', 'url':"prodaji"},
#     {'title':'Отдел снабжения', 'url':"snab"},
#     ]
#     return main_menu
@register.inclusion_tag('main/tags/show_main_menu.html')
def show_main_menu(key='Главная'):
    main_menu = [
        {'title': 'Главная', 'url': "home"},
        {'title': 'ДКО', 'url': "dko"},
        {'title': 'Отдел продаж', 'url': "prodaji"},
        {'title': 'Отдел снабжения', 'url': "snab"},
        {'title': 'Регистрация', 'url': "registration"},
    ]

    return {'main_menu':main_menu, 'key':key,}


@register.inclusion_tag('main/tags/show_sidebar.html')
def show_sidebar():
    side_bar = SideBar.objects.all()
    return {'side_bar':side_bar,}

