from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    sorting = request.GET.get('sort')
    if sorting:
        if sorting == 'name':
            phones = phones.order_by('name')
        elif sorting == 'min_price':
            phones = phones.order_by('price')
        elif sorting == 'max_price':
            phones = phones.order_by('-price')
    context = {
        'phones': phones,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.all().filter(slug=slug)[0]
    context = {
        'phone': phone,
    }
    return render(request, template, context)
