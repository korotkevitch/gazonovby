# Generated by Django 3.2.3 on 2021-05-31 14:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, verbose_name='Название в шапке страницы')),
                ('subtitle', models.CharField(blank=True, max_length=70, verbose_name='Подзаголовок перед текстом')),
                ('text', models.TextField(verbose_name='Текст о компании')),
                ('slug', models.SlugField(max_length=70, unique=True)),
                ('image_head', models.FileField(blank=True, upload_to='', verbose_name='Фото в шапке')),
                ('image_text', models.FileField(blank=True, upload_to='', verbose_name='Фото в тексте')),
            ],
            options={
                'verbose_name': 'О компании',
                'verbose_name_plural': 'О компании',
            },
        ),
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catalog_name', models.CharField(blank=True, max_length=50, verbose_name='Название раздела')),
                ('text', models.TextField(verbose_name='Вступление')),
                ('slug', models.SlugField(max_length=70, unique=True)),
                ('image_head', models.FileField(blank=True, upload_to='', verbose_name='Фото в шапке')),
                ('image_text', models.FileField(blank=True, upload_to='', verbose_name='Фото на странице')),
            ],
            options={
                'verbose_name': 'Каталог',
                'verbose_name_plural': 'Каталог',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(blank=True, max_length=50, verbose_name='Категория товара')),
                ('description', models.CharField(blank=True, max_length=70, verbose_name='Описание категории')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('image_head', models.FileField(blank=True, upload_to='', verbose_name='Фото в шапке')),
                ('image_text', models.FileField(blank=True, upload_to='', verbose_name='Фото на странице')),
                ('icon_code', models.CharField(blank=True, max_length=30, verbose_name='Код флатикона')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='Имя')),
                ('phone', models.CharField(blank=True, max_length=50, verbose_name='Телефон')),
                ('message', models.TextField(blank=True, max_length=500, verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Сообщение с формы заказа',
                'verbose_name_plural': 'Сообщения с формы заказа',
            },
        ),
        migrations.CreateModel(
            name='FeedbackPhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Дата')),
                ('phone', models.CharField(blank=True, max_length=50, verbose_name='Телефон')),
            ],
            options={
                'verbose_name': 'Сообщение с просьбой позвонить',
                'verbose_name_plural': 'Сообщения с просьбой позвонить',
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, verbose_name='Название раздела')),
                ('subtitle', models.CharField(blank=True, max_length=30, verbose_name='Подраздел')),
                ('price_item', models.CharField(blank=True, max_length=30, verbose_name='Тариф')),
                ('price_content', models.TextField(blank=True, verbose_name='Описание тарифа')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Цена')),
                ('slug', models.SlugField(max_length=70, unique=True)),
                ('image_head', models.FileField(blank=True, upload_to='', verbose_name='Фото в шапке')),
                ('image_text', models.FileField(blank=True, upload_to='', verbose_name='Фото тарифа')),
            ],
            options={
                'verbose_name': 'Прайс-лист',
                'verbose_name_plural': 'Прайс-лист',
            },
        ),
        migrations.CreateModel(
            name='ServiceCat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(blank=True, max_length=50, verbose_name='Категория услуги')),
                ('description', models.CharField(blank=True, max_length=70, verbose_name='Описание категории')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('image_head', models.FileField(blank=True, upload_to='', verbose_name='Фото в шапке')),
                ('image_text', models.FileField(blank=True, upload_to='', verbose_name='Фото на странице')),
                ('icon_code', models.CharField(blank=True, max_length=30, verbose_name='Код иконки')),
            ],
            options={
                'verbose_name': '   Категория услуги',
                'verbose_name_plural': '  Категории услуг',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory', models.CharField(blank=True, max_length=30, verbose_name='Подкатегория')),
                ('prefix', models.CharField(blank=True, max_length=30, verbose_name='Префикс')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, verbose_name='Цена')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('image_head', models.FileField(blank=True, upload_to='', verbose_name='Фото в шапке')),
                ('image_service', models.FileField(blank=True, upload_to='', verbose_name='Фото услуги')),
                ('service_name', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='gazon.servicecat')),
            ],
            options={
                'verbose_name': ' Услуга',
                'verbose_name_plural': ' Услуги',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory', models.CharField(blank=True, max_length=30, verbose_name='Подкатегория')),
                ('prefix', models.CharField(blank=True, max_length=30, verbose_name='Префикс')),
                ('product_name', models.CharField(blank=True, max_length=70, verbose_name='Название')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, verbose_name='Цена')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('image_head', models.FileField(blank=True, upload_to='', verbose_name='Фото в шапке')),
                ('image_product', models.FileField(blank=True, upload_to='', verbose_name='Фото')),
                ('category', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='gazon.category')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
