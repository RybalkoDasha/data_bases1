from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')

def show_catalog(request):
    phones = Phone.objects.all()
    template = 'catalog.html'
    context = {
        'phones' : phones
    }
    return render(request, template, context)

def show_product(request, slug):
    phone_slug = Phone.objects.filter(slug = slug)[0]
    template = 'product.html'
    context = {'phone' : phone_slug}
    return render(request, template, context)
