from django.shortcuts import render, get_object_or_404, Http404
from django.views.generic import View
from settings.models import Banner
from .models import ProductCategory, Product, Look


class Index(View):

    def get(self, request):
        context = {}
        context['banners'] = Banner.objects.all()
        context['categories'] = ProductCategory.objects.all()
        context['products'] = Product.displayed.all()[:6]
        context['looks'] = Look.objects.all()[:5]
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


class Lookbook(View):
    def get(self, request):
        context = {}
        context['looks'] = Look.objects.all()
        return render(request, 'lookbook.html', context)


class Delivery(View):
    def get(self, request):
        context = {}
        return render(request, 'delivery.html', context)


class About(View):
    def get(self, request):
        context = {}
        return render(request, 'about.html', context)



def product_detail(request, product_id):
    context = {}
    context['target'] = Product.displayed.get(id=product_id)
    print(context['target'])
    return render(request, 'product_detail.html', context)


class LookDetail(View):
    def get(self, request, look_id):
        context = {}
        return render(request, 'look_detail.html', context)
