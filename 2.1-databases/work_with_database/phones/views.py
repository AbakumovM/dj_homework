from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from phones.models import Phone
from rest_framework.response import Response

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phone_object = Phone.objects.all()
    sort_map = {
        'min_price': 'price',
        'max_price': '-price',
        'name': 'name',
    }
    context = {'phones': phone_object}
    sort = request.GET.get('sort')
    if sort:
        phones = phone_object.order_by(sort_map[sort])
        context = {'phones': phones}
        return render(request, template, context)
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    phone_object = Phone.objects.filter(slug=slug)
    context.setdefault('phone', [{'name': i.name, 'price': i.price, 'image': i.image, 'release_date': i.release_date, 'lte_exists': i.lte_exists, 'slug': i.slug} for i in phone_object][0])
    return render(request, template, context)

@api_view(['GET'])
def sample_view(request):
    return Response('Привет, как дела?')