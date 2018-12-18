from django.shortcuts import render, Http404, HttpResponse
from django.views.generic import View
from settings.models import Banner, DeliveryPaymentInfo
from .models import ProductCategory, Product, ContactPerson

import json
import random

def random_queryset(class_name, number, except_id=None):
    """returns queryset of random [number] items of given class"""
    ids = list(class_name.displayed.values_list('id', flat=True))
    print(ids)
    if except_id:
        ids.remove(int(except_id))
    try:
        random_ids = random.sample(ids, number)
    except ValueError:
        random_ids = []
    queryset = class_name.displayed.filter(id__in=random_ids)
    return queryset


class Index(View):

    def get(self, request):
        context = {}
        context['banners'] = Banner.objects.all()
        context['categories'] = ProductCategory.objects.all()
        context['products'] = Product.displayed.all()[:6]
        return render(request, 'index.html', context)


class Catalog(View):

    def get(self, request, category):
        context = {}
        if category == 'all':
            products = Product.objects.all()
        else:
            products = Product.displayed.filter(category_id=int(category))
        context['products'] = products
        context['categories'] = ProductCategory.objects.all()
        return render(request, 'catalog.html', context)


class Delivery(View):
    def get(self, request):
        info = DeliveryPaymentInfo.objects.all()
        context = {'info': info}
        return render(request, 'delivery.html', context)

def product_detail(request, product_id):
    context = {}
    context['target'] = Product.displayed.get(id=product_id)
    context['suggestions'] = random_queryset(Product, 6, product_id)
    return render(request, 'product_detail.html', context)


def contact_us(request):
    if request.method == 'POST' and request.is_ajax():
        name, phone = request.POST['name'], request.POST['phone']
        person = ContactPerson.objects.create(name=name, phone=phone)
        response = {}
        return HttpResponse(json.dumps(response))
    else:
        raise Http404