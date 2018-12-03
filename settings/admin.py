from django.contrib import admin
from .models import Banner, IconsPack, SiteMain


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    pass


@admin.register(IconsPack)
class IconsPack(admin.ModelAdmin):
    pass


@admin.register(SiteMain)
class SiteMainAdmin(admin.ModelAdmin):
    pass