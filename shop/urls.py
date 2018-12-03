from django.urls import path
from .views import (Index, Catalog, Lookbook, Delivery, About, product_detail,
                    LookDetail)


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('catalog/category=<slug:category>', Catalog.as_view(), name='catalog'),
    path('catalog/products/<int:product_id>', product_detail, name='product_detail'),
    path('lookbook', Lookbook.as_view(), name='lookbook'),
    path('lookbook/<int:look_id>', LookDetail.as_view(), name='look_detail'),
    path('about', About.as_view(), name='about'),
    path('delivery', Delivery.as_view(), name='delivery'),
]