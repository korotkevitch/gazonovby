# Generated by Django 3.2.3 on 2021-06-02 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gazon', '0009_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='service',
            field=models.CharField(blank=True, max_length=100, verbose_name='Название услуги'),
        ),
    ]