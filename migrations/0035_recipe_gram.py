# Generated by Django 3.2.9 on 2021-12-04 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0034_auto_20211204_0911'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='gram',
            field=models.CharField(default=1, max_length=10, verbose_name='Укажите кол-во грамм, шт или мл'),
            preserve_default=False,
        ),
    ]
