# Generated by Django 3.2.9 on 2021-12-04 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0033_auto_20211204_0623'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='cooking',
            field=models.TextField(default='Как приготовить блюдо', verbose_name='Инструкция по приготовлению'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='number',
            field=models.IntegerField(verbose_name='Количество порций'),
        ),
    ]
