# Generated by Django 3.2.9 on 2021-11-27 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0010_alter_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/recipes/%Y/%m/%d', verbose_name='Ссылка картинки'),
        ),
    ]