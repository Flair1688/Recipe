# Generated by Django 3.2.9 on 2021-12-04 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0039_auto_20211205_0332'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='gramm',
            new_name='gram',
        ),
    ]