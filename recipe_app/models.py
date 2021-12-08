from django.db import models
from django.contrib.auth.models import User


class Avatar(models.Model):
    image = models.ImageField(blank=True, upload_to='avatar/%Y/%m/%d', verbose_name='Аватарка')

class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name='Категория блюда')

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    ingredient_title = models.CharField(max_length=30)

    def __str__(self):
        return self.ingredient_title



class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False, verbose_name="Автор")
    create = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=150, verbose_name="Название блюда")
    description = models.TextField(null=True, blank=False, verbose_name="Описание")
    video = models.FileField(upload_to='videos/%Y/%m/%d', blank=True, null=True, verbose_name="Видео")
    image = models.ImageField(blank=False, upload_to='images/%Y/%m/%d', verbose_name='Изображение')
    number = models.IntegerField(verbose_name="Количество порций", blank=False)
    ingredient = models.ManyToManyField(Ingredient, blank=False, verbose_name="Ингредианты")
    gram = models.TextField(max_length=300, blank=False, verbose_name="Укажите кол-во грамм, шт или мл. Каждого инградиента")
    cooking = models.TextField(blank=False, verbose_name="Инструкция по приготовлению")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=False, verbose_name="Категория блюда")





    def __str__(self):
        return self.title



class Meta:
    verbose_name = "Рецепты"
    verbose_name_plural = "Рецепты"

