# Generated by Django 3.2.3 on 2021-06-02 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gazon', '0010_alter_service_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='service',
            field=models.CharField(blank=True, max_length=50, verbose_name='Название услуги'),
        ),
        migrations.AlterField(
            model_name='service',
            name='title',
            field=models.CharField(blank=True, max_length=100, verbose_name='Наши услуги'),
        ),
    ]
