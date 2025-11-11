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
    'butter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты
}

def home_view(request):
    pages = {}
    for page in DATA.keys():
        pages[page.capitalize()] = f'{page}/'
    context = {
        'pages': pages
    }

    return render(request, 'home.html', context)


def recipes(request, recipe_path):
    # ?servings=4
    ingredients = {}
    servings = request.GET.get("servings")
    if servings:
        for ingredient, amount in list(DATA[recipe_path].items()):
            ingredients[ingredient] = amount * int(servings)
    else:
        ingredients = DATA[recipe_path]
    context = {
        'recipe': recipe_path,
        'ingredients': ingredients,
    }
    return render(request, 'recipe.html', context)
