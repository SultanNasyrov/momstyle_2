from django.db import models


class Banner(models.Model):
    """Contains images for banner app on index page of the site"""

    image = models.ImageField(upload_to='banner/', verbose_name='Изображение, размер ~ 300 КБ')
    image_mini = models.ImageField(upload_to='banner/', verbose_name='Изображение(миниатюра), размер ~ 10 КБ')
    position = models.PositiveSmallIntegerField(default=1, verbose_name='Позиция')

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'
        ordering = ['position']

    def __str__(self):
        return 'Баннер {}'.format(self.position)


class SiteMain(models.Model):

    logo = models.ImageField(upload_to='logo/', verbose_name='Логотип', null=True, blank=True)
    sizes_table = models.ImageField(upload_to='sizes/', null=True, blank=True, verbose_name='Таблица размеров')

    category_h2 = models.CharField(max_length=100, null=True, blank=True, verbose_name='Название блока категории')
    category_par = models.CharField(max_length=300, null=True, blank=True, verbose_name='Описание блока категории')
    product_h2 = models.CharField(max_length=100, null=True, blank=True, verbose_name='Название блока продукты')
    product_par = models.CharField(max_length=300, null=True, blank=True, verbose_name='Описание блока продукты')

    vk_url = models.URLField(blank=True, null=True, verbose_name='Ссылка на страницу вк')
    insta_url = models.URLField(blank=True, null=True, verbose_name='Ссылка на страницу инстаграм')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона', null=True, blank=True)
    email = models.EmailField(null=True, blank=True, verbose_name='Электронный адрес')
    address = models.CharField(max_length=500, null=True, blank=True, verbose_name='Адрес')
    working_hours = models.CharField(max_length=100, null=True, blank=True, verbose_name='Часы работы')
    delivery_header_image = models.ImageField(upload_to='header_images/', verbose_name='Изображение страницы доставка',
                                              null=True, blank=True)
    about_header_image = models.ImageField(upload_to='header_images/', verbose_name='Изображение страницы о нас',
                                           null=True, blank=True)

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
    vk = models.FileField(upload_to='icons/', verbose_name='Вконтакте', null=True, blank=True)
    instagram = models.FileField(upload_to='icons/', verbose_name='Инстаграм', null=True, blank=True)
    cart = models.FileField(upload_to='icons/', verbose_name='Корзина', null=True, blank=True)
    up = models.FileField(upload_to='icons/', verbose_name='Вверх', null=True, blank=True)

    # footer
    footer_phone = models.FileField(upload_to='icons/', null=True, blank=True, verbose_name='Телефон(футер)')
    footer_email = models.FileField(upload_to='icons/', null=True, blank=True, verbose_name='Email(футер)')
    footer_address = models.FileField(upload_to='icons/', null=True, blank=True, verbose_name='Адрес(футер)')
    footer_time = models.FileField(upload_to='icons/', null=True, blank=True, verbose_name='Время работы(футер)')

    class Meta:
        verbose_name = 'Набор иконок'
        verbose_name_plural = 'Набор иконок'

    def __str__(self):
        return 'Набор иконок'


class Seo(models.Model):

    index_title = models.CharField(max_length=80, verbose_name='Title(Главная страница)', null=True, blank=True)
    index_description = models.CharField(max_length=200, verbose_name='Description(Главная страница)', null=True, blank=True)
    index_h1 = models.CharField(max_length=500, verbose_name='h1(Главная страница)', null=True, blank=True)
    catalog_title = models.CharField(max_length=80, verbose_name='Title(Каталог)', null=True, blank=True)
    catalog_description = models.CharField(max_length=200, verbose_name='Description(Каталог)', null=True, blank=True)
    product_title = models.CharField(max_length=80, verbose_name='Title(Главная страница)', null=True, blank=True)
    product_description = models.CharField(max_length=200, verbose_name='Description(Главная страница)', null=True, blank=True)
    delivery_title = models.CharField(max_length=80, verbose_name='Title(Доставка)', null=True, blank=True)
    delivery_description = models.CharField(max_length=200, verbose_name='Description(Доставка)', null=True, blank=True)
    delivery_h1 = models.CharField(max_length=500, verbose_name='h1(Доставка)', null=True, blank=True)
    about_title = models.CharField(max_length=80, verbose_name='Title(О нас)', null=True, blank=True)
    about_description = models.CharField(max_length=200, verbose_name='Description(О нас)', null=True, blank=True)
    about_h1 = models.CharField(max_length=500, verbose_name='h1(О нас)', null=True, blank=True)
    cart_title = models.CharField(max_length=80, verbose_name='Title(Корзина)', null=True, blank=True)
    cart_description = models.CharField(max_length=200, verbose_name='Description(Корзина)', null=True, blank=True)
    cart_h1 = models.CharField(max_length=500, verbose_name='h1(Корзина)', null=True, blank=True)

    class Meta:
        verbose_name = 'Настройки SEO'
        verbose_name_plural = 'Настройки SEO'

    def __str__(self):
        return 'Настройки'
