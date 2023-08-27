from django.shortcuts import render
from django.http import HttpResponse

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
    'butter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def recipe(request, dish):
    # user_request = DATA.get(dish, 'Not found')
    # total_ordered_dish = [f'<li>{k} : {v}</li>' for k, v in user_request.items()]
    # return HttpResponse(total_ordered_dish)

    quantity = int(request.GET.get('servings', 1))
    ordered_dish = DATA.get(dish).items()
    total_ordered_dish = dict()
    for k, v in ordered_dish:
        total_ordered_dish[k] = round(v * quantity, 2)
    context = dict(recipe = total_ordered_dish, dish = dish, quantity = quantity)
    return render(request, 'calculator/index.html', context)




