from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
def calculate_views(request, recipes_list):
    template_name = 'calculator/index.html'
    if recipes_list in DATA:
        data = DATA[recipes_list]
        servings = request.GET.get('servings', None)
        if servings:
           result = dict()
           for key, value in data.items():
               news_value = value * servings
               result[key] = news_value
           context = {
                'recipes_list': recipes_list,
                'recipe': result,
        }
        else:
            context ={
                'recipes_list': recipes_list,
                'recipe': data,
            }
    else:
        context = None

    return render(request, template_name, context=context)
def all_home_view(request):
    template_name = 'home/home.html'
    all_recipes = list(DATA.keys())
    context = {
        'all_recipes': all_recipes,
    }
    return render(request, template_name, context=context)
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
