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
    category_h2 = models.CharField(max_length=100, null=True, blank=True, verbose_name='Название блока категории')
    category_par = models.CharField(max_length=300, null=True, blank=True, verbose_name='Описание блока категории')
    product_h2 = models.CharField(max_length=100, null=True, blank=True, verbose_name='Название блока продукты')
    product_par = models.CharField(max_length=300, null=True, blank=True, verbose_name='Описание блока продукты')
    look_h2 = models.CharField(max_length=100, null=True, blank=True, verbose_name='Название блока луки')
    look_par = models.CharField(max_length=300, null=True, blank=True, verbose_name='Описание блока луки')

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

    product_loupe = models.FileField(upload_to='icons/', verbose_name='Лупа(карточка продукта)', null=True, blank=True)
    next = models.FileField(upload_to='icons/', verbose_name='Следующий продукт', null=True, blank=True)



class Seo(models.Model):

    index_title = models.CharField(max_length=80, default='', verbose_name='Title(Главная страница)',
                                   null=True, blank=True)
    index_description = models.CharField(max_length=200, default='', verbose_name='Description(Главная страница)',
                                         null=True, blank=True)
    index_h1 = models.CharField(max_length=500, default='', verbose_name='h1(Главная страница)',
                                null=True, blank=True)

    catalog_title = models.CharField(max_length=80, default='', verbose_name='Title(Каталог)',
                                     null=True, blank=True)
    catalog_description = models.CharField(max_length=200, default='', verbose_name='Description(Каталог)',
                                           null=True, blank=True)

    product_title = models.CharField(max_length=80, default='', verbose_name='Title(Главная страница)',
                                     null=True, blank=True)
    product_description = models.CharField(max_length=200, default='', verbose_name='Description(Главная страница)',
                                           null=True, blank=True)

    lookbook_title = models.CharField(max_length=80, default='', verbose_name='Title(Лубук)',
                                      null=True, blank=True)
    lookbook_description = models.CharField(max_length=200, default='', verbose_name='Description(Лукбук)',
                                            null=True, blank=True)
    lookbook_h1 = models.CharField(max_length=500, default='', verbose_name='h1(Лукбук)',
                                   null=True, blank=True)

    look_title = models.CharField(max_length=80, default='', verbose_name='Title(Лук)',
                                  null=True, blank=True)
    look_description = models.CharField(max_length=200, default='', verbose_name='Description(Лук)',
                                        null=True, blank=True)

    delivery_title = models.CharField(max_length=80, default='', verbose_name='Title(Доставка)',
                                      null=True, blank=True)
    delivery_description = models.CharField(max_length=200, default='', verbose_name='Description(Доставка)',
                                            null=True, blank=True)
    delivery_h1 = models.CharField(max_length=500, default='', verbose_name='h1(Доставка)',
                                   null=True, blank=True)

    about_title = models.CharField(max_length=80, default='', verbose_name='Title(О нас)',
                                   null=True, blank=True)
    about_description = models.CharField(max_length=200, default='', verbose_name='Description(О нас)',
                                         null=True, blank=True)
    about_h1 = models.CharField(max_length=500, default='', verbose_name='h1(О нас)',
                                null=True, blank=True)

    cart_title = models.CharField(max_length=80, default='', verbose_name='Title(Корзина)', null=True, blank=True)
    cart_description = models.CharField(max_length=200, default='', verbose_name='Description(Корзина)',
                                        null=True, blank=True)
    cart_h1 = models.CharField(max_length=500, default='', verbose_name='h1(Корзина)', null=True, blank=True)
