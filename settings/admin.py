from django.contrib import admin
from .models import Banner, IconsPack, SiteMain, Seo


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    pass


@admin.register(IconsPack)
class IconsPack(admin.ModelAdmin):
    pass


@admin.register(SiteMain)
class SiteMainAdmin(admin.ModelAdmin):
    pass


@admin.register(Seo)
class Seo(admin.ModelAdmin):
    pass