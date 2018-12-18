from django.contrib import admin
from .models import Banner, IconsPack, SiteMain, Seo, DeliveryPaymentInfo


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    pass


@admin.register(IconsPack)
class IconsPackAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Базовые', {'fields': ('cart', 'up', 'like')} ),
        ('Соц. сети', {'fields': ('vk', 'instagram')} ),
        ('Подвал', {'fields': ('footer_phone', 'footer_email', 'footer_address', 'footer_time')} ),
    )


@admin.register(SiteMain)
class SiteMainAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Базовые', {'fields': ('logo', )}),
        ('Текст', {'fields': (('category_h2', 'category_par'), ('product_h2', 'product_par'))}),
        ('Ссылки', {'fields': ('insta_url', 'vk_url')}),
        ('Контакты', {'fields': ('phone_number', 'email', 'address', 'working_hours')}),
        ('Остальное', {'fields': ('delivery_header_image', 'about_header_image')}),

    )


@admin.register(Seo)
class SeoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Главная страница', {'fields': ('index_title', 'index_description', 'index_h1')}),
        ('Каталог', {'fields': ('catalog_title', 'catalog_description')}),
        ('Страница товара', {'fields': ('product_title', 'product_description')}),
        ('Страница доставки', {'fields': ('delivery_title', 'delivery_description', 'delivery_h1')}),
        ('Страница о нас', {'fields': ('about_title', 'about_description', 'about_h1')}),
        ('Страница поста', {'fields': ('post_title', 'post_description')}),
        ('Страница корзины', {'fields': ('cart_title', 'cart_description', 'cart_h1')}),
    )


@admin.register(DeliveryPaymentInfo)
class DeliveryPaymentInfoAdmin(admin.ModelAdmin):
    list_display = ['title', 'type']