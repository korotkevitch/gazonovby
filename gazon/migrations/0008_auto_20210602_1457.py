# Generated by Django 3.2.3 on 2021-06-02 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gazon', '0007_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='intro',
            field=models.CharField(blank=True, max_length=50, verbose_name='Вступительная фраза'),
        ),
        migrations.AlterField(
            model_name='about',
            name='title',
            field=models.CharField(blank=True, max_length=50, verbose_name='Заголовок'),
        ),
    ]
