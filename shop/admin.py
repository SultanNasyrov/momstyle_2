from django.contrib import admin
from .models import (ProductSize, ProductCategory, Product, ProductImage,
                     Look, LookImage, Order, OrderItem)


@admin.register(ProductSize)
class ProductSizeAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    pass


class ProductImageTabular(admin.TabularInline):
    model = ProductImage
    extra = 0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category','price_no_sale', 'price_sale', 'material', 'display']
    list_editable = ['display']
    list_filter = ['category', 'price_sale', 'display']
    search_fields = ['name', 'material']
    inlines = [ProductImageTabular]


class LookImageTabular(admin.TabularInline):
    model = LookImage
    extra = 0


@admin.register(Look)
class LookAdmin(admin.ModelAdmin):
    inlines = [LookImageTabular]

class OrderItemTabular(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemTabular]






