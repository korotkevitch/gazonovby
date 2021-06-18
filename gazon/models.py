from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify
from django.utils.safestring import mark_safe
from django.shortcuts import reverse


class Gallery(models.Model):
    intro = models.CharField('Вступительная фраза', max_length=30, blank=True)
    header = models.CharField('Заголовок раздела', max_length=50, blank=True)
    image_1 = models.FileField('Фото х1', blank=True)
    image_2 = models.FileField('Фото х2', blank=True)
    image_big = models.FileField('Фото по клику', blank=True)
    title = models.CharField('Название фотографии', max_length=30, blank=True)
    service = models.CharField('Название услуги', max_length=30, blank=True)
    description = models.CharField('Описание фотографии', max_length=200, blank=True)

    def image_1_preview(self):
        if self.image_1:
            return mark_safe('<img src="%s" style="width:100px; height:100px;" />' % self.image_1.url)
        else:
            return 'Нет фото'

    image_1_preview.short_description = 'Фото х1'

    def image_2_preview(self):
        if self.image_2:
            return mark_safe('<img src="%s" style="width:100px; height:100px;" />' % self.image_2.url)
        else:
            return 'Нет фото'

    image_2_preview.short_description = 'Фото х2'

    def image_big_preview(self):
        if self.image_big:
            return mark_safe('<img src="%s" style="width:100px; height:80px;" />' % self.image_big.url)
        else:
            return 'Нет фото'

    image_big_preview.short_description = 'Фото по клику'

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерея'

    def __str__(self):
        return self.title


class Head(models.Model):
    image = models.FileField('Большое фото в шапке', blank=True)
    logo = models.FileField('Логотип', blank=True)
    welcome = models.CharField('Приветствие', max_length=30, blank=True)
    text = models.CharField('Крупный текст на фото', max_length=120, blank=True)

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:100px; height:100px;" />' % self.image.url)
        else:
            return 'Нет фото'

    image_preview.short_description = 'Главное фото'

    def logo_preview(self):
        if self.logo:
            return mark_safe('<img src="%s" style="width:100px; height:100px;" />' % self.logo.url)
        else:
            return 'Нет фото'

    logo_preview.short_description = 'Логотип'

    class Meta:
        verbose_name = '      Шапка'
        verbose_name_plural = '      Шапка'

    def __str__(self):
        return self.welcome


class About(models.Model):
    intro = models.CharField('Вступительная фраза', max_length=50, blank=True)
    title = models.CharField('Заголовок', max_length=50, blank=True)
    text = models.CharField('Текст о компании', max_length=800, blank=True)

    class Meta:
        verbose_name = '     О компании'
        verbose_name_plural = '     О компании'

    def __str__(self):
        return self.title


class Service(models.Model):
    intro = models.CharField('Вступительная фраза', max_length=50, blank=True)
    title = models.CharField('Название раздела', max_length=100, blank=True)
    service = models.CharField('Название услуги', max_length=50, blank=True)
    description = models.CharField('Описание услуги', max_length=500, blank=True)
    icon = models.CharField('Код флатикона', max_length=50, blank=True)

    class Meta:
        verbose_name = '    Услуга'
        verbose_name_plural = '    Услуги'

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    name = models.CharField('Имя, фамилия', max_length=50, blank=True)
    testimonial = models.CharField('Отзыв', max_length=300, blank=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField('Имя', max_length=50, blank=True)
    phone = models.CharField('Телефон', max_length=50, blank=True)
    message = models.TextField('Сообщение', max_length=500, blank=True)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return self.name