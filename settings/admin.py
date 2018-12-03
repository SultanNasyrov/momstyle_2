from django.contrib import admin
from .models import Banner, IconsPack


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    pass

@admin.register(IconsPack)
class IconsPack(admin.ModelAdmin):
    pass