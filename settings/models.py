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

    def __str__(self):
        return 'Баннер {}'.format(self.position)


class SiteMain(models.Model):

    logo = models.ImageField(upload_to='logo/', verbose_name='Логотип', null=True, blank=True)

    lookbook_header_image = models.ImageField(upload_to='header_images/', verbose_name='Изображение страницы лукбук',
                                              null=True, blank=True)
    delivery_header_image = models.ImageField(upload_to='header_images/', verbose_name='Изображение страницы доставка',
                                              null=True, blank=True)
    about_header_image = models.ImageField(upload_to='header_images/', verbose_name='Изображение страницы о нас',
                                           null=True, blank=True)

    map = models.TextField(default='', verbose_name='Код карты', null=True, blank=True)

    class Meta:
        verbose_name = 'Настройки сайта'
        verbose_name_plural = 'Настройки сайта'

    def __str__(self):
        return 'Настройки'


class IconsPack(models.Model):
    """
    Singleton
    Contains all icons used in site

    """
    navbar_vk = models.FileField(upload_to='icons/', verbose_name='Вконтакте(навигация)', null=True, blank=True)
    navbar_instagram = models.FileField(upload_to='icons/', verbose_name='Инстаграм(навигация)', null=True, blank=True)
    navbar_cart = models.FileField(upload_to='icons/', verbose_name='Корзина(навигация)', null=True, blank=True)


class Seo(models.Model):

    index_title = models.CharField(max_length=80, default='', verbose_name='Title(Главная страница)')
    index_description = models.CharField(max_length=200, default='', verbose_name='Description(Главная страница)')
    index_h1 = models.CharField(max_length=500, default='', verbose_name='h1(Главная страница)')

    catalog_title = models.CharField(max_length=80, default='', verbose_name='Title(Каталог)')
    catalog_description = models.CharField(max_length=200, default='', verbose_name='Description(Каталог)')

    product_title = models.CharField(max_length=80, default='', verbose_name='Title(Главная страница)')
    product_description = models.CharField(max_length=200, default='', verbose_name='Description(Главная страница)')

    lookbook_title = models.CharField(max_length=80, default='', verbose_name='Title(Лубук)')
    lookbook_description = models.CharField(max_length=200, default='', verbose_name='Description(Лукбук)')
    lookbook_h1 = models.CharField(max_length=500, default='', verbose_name='h1(Лукбук)')

    look_title = models.CharField(max_length=80, default='', verbose_name='Title(Лук)')
    look_description = models.CharField(max_length=200, default='', verbose_name='Description(Лук)')

    delivery_title = models.CharField(max_length=80, default='', verbose_name='Title(Доставка)')
    delivery_description = models.CharField(max_length=200, default='', verbose_name='Description(Доставка)')
    delivery_h1 = models.CharField(max_length=500, default='', verbose_name='h1(Доставка)')

    about_title = models.CharField(max_length=80, default='', verbose_name='Title(О нас)')
    about_description = models.CharField(max_length=200, default='', verbose_name='Description(О нас)')
    about_h1 = models.CharField(max_length=500, default='', verbose_name='h1(О нас)')

    cart_title = models.CharField(max_length=80, default='', verbose_name='Title(Корзина)')
    cart_description = models.CharField(max_length=200, default='', verbose_name='Description(Корзина)')
    cart_h1 = models.CharField(max_length=500, default='', verbose_name='h1(Корзина)')
