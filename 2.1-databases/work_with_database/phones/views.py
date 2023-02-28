from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    context = {}
    phone_object = list(Phone.objects.values())
    context.setdefault('phones', phone_object)
    if request.GET.get('sort', None) == 'min_price':
        context['phones'].sort(key=lambda item: item['price'])
        return render(request, template, context)
    elif request.GET.get('sort', None) == 'max_price':
        context['phones'].sort(key=lambda item: item['price'], reverse=True)
        return render(request, template, context)
    elif request.GET.get('sort', None) == 'name':
        context['phones'].sort(key=lambda item: item['name'])
        return render(request, template, context)
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    phone_object = Phone.objects.filter(slug=slug)
    context.setdefault('phone', [{'name': i.name, 'price': i.price, 'image': i.image, 'release_date': i.release_date, 'lte_exists': i.lte_exists, 'slug': i.slug} for i in phone_object][0])
    return render(request, template, context)
