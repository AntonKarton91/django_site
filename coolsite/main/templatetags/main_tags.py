from django import template

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
    ]
    return {'main_menu':main_menu, 'key':key}

