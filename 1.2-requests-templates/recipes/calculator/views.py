from django.shortcuts import render
from django.shortcuts import render, reverse

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
}

def home_view(request):
    template_name = 'calculator/home.html'
    pages = {
        'Рецепт приготовления омлета': reverse('omlet'),
        'Рецет приготовления пасты': reverse('pasta'),
        'Рецепт приготовления бутерброда': reverse('buter')
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def get_omlet(request):
    servings = int(request.GET.get('servings', 1))
    context = {}
    context.setdefault('recipe', {ing : count * servings for ing, count in DATA['omlet'].items()})
    return render(request, 'calculator/index.html', context)

def get_pasta(request):
    servings = int(request.GET.get('servings', 1))
    context = {}
    context.setdefault('recipe', {ing : count * servings for ing, count in DATA['pasta'].items()})
    return render(request, 'calculator/index.html', context)


def get_buter(request):
    servings = int(request.GET.get('servings', 1))
    context = {}
    context.setdefault('recipe', {ing : count * servings for ing, count in DATA['buter'].items()})
    return render(request, 'calculator/index.html', context)
