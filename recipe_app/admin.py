from django.contrib import admin
from .models import Recipe, Ingredient, Category, Avatar
from django.forms import CheckboxSelectMultiple
from django.db import models


# Checkbox for many-to-many fields
class IngredientAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }


admin.site.register(Recipe, IngredientAdmin)
admin.site.register(Ingredient)
admin.site.register(Category)
admin.site.register(Avatar)





