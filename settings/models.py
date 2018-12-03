from django.db import models


class Banner(models.Model):
    """Contains images for banner app on index page of the site"""

    image = models.ImageField(upload_to='banner/', verbose_name='Изображение, размер ~ 300 КБ')
    image_mini = models.ImageField(upload_to='banner/', verbose_name='Изображение(миниатюра), размер ~ 70 КБ')
    position = models.PositiveSmallIntegerField(default=1, verbose_name='Позиция')

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'
        ordering = ['position']


class SiteMain(models.Model):
    pass


class PageSeoConfiguration(models.Model):
    pass


class IconsPack(models.Model):
    """
    Singleton
    Contains all icons used in site

    """
    navbar_vk = models.FileField(upload_to='icons/', verbose_name='Вконтакте(навигация)')
    navbar_instagram = models.FileField(upload_to='icons/', verbose_name='Инстаграм(навигация)')
    navbar_cart = models.FileField(upload_to='icons/', verbose_name='Корзина(навигация)')
