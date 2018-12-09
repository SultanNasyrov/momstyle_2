from django.urls import path
from .views import (Index, Catalog, Delivery, About, product_detail, contact_us)


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('catalog/category=<slug:category>', Catalog.as_view(), name='catalog'),
    path('catalog/products/<int:product_id>', product_detail, name='product_detail'),
    path('about', About.as_view(), name='about'),
    path('delivery', Delivery.as_view(), name='delivery'),
    path('contact-us', contact_us, name='contact-us')
]