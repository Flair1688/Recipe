from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_filters.rest_framework import DjangoFilterBackend
from .models import Recipe, Ingredient, Category, Avatar

class IngredientCategory:
    # Фильтер по инградиентам и категории блюда
    def get_ingredient(self):
        return Ingredient.objects.all()

    def get_category(self):
        return Category.objects.all()

    def get_user(self):
        return Avatar.objects.all()




class RecipeList(IngredientCategory, ListView):
    model = Recipe
    filter_backends = (DjangoFilterBackend,)


class PersonalAreaList(IngredientCategory, ListView):
    model = Recipe
    context_object_name = 'recipes'
    template_name = 'recipe_app/personal_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipes'] = context['recipes'].filter(user=self.request.user)

        return context

class AuthorsList(IngredientCategory, ListView):
    model = Avatar
    context_object_name = 'authors'
    template_name = 'recipe_app/authors_list.html'



class RecipeDetailView(IngredientCategory, DetailView):
    model = Recipe
    template_name = 'recipe_app/recipe_detail.html'

class AuthorDetailView(IngredientCategory, ListView):
    model = Recipe
    context_object_name = 'author'
    template_name = 'recipe_app/author_detail.html'

    def recipe(request):
        context = {
            'users': User.objects.filter(author=request.user)
        }

        return render(request, 'author_detail.html', context)



class Search(IngredientCategory, ListView):
    context_object_name = 'search'


    # paginate_by = 7 #кол-во выводимых записей
    def get_queryset(self):

        search = Recipe.objects.filter(
            title__iregex=self.request.GET.get("q"))

        return search

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, *kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'

        return context

class FilterRecipeView(IngredientCategory, ListView):
    # Фильтер рецептов
    def get_queryset(self):
        queryset = Recipe.objects.filter(
            Q(ingredient__in=self.request.GET.getlist("ingredient")) |
            Q(category__in=self.request.GET.getlist("category"))
        ).distinct()
        return queryset

class CustomLoginView(IngredientCategory, LoginView):
    template_name = 'recipe_app/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('personal_list')

class RegisterPage(IngredientCategory, FormView):
    template_name = 'recipe_app/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('personal_list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('recipes')
        return super(RegisterPage, self).get(*args, **kwargs)


class RecipeCreate(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ['title', 'description', 'video', 'image', 'number', 'ingredient', 'gram', 'cooking', 'category']
    template_name = 'recipe_app/recipe_form.html'
    success_url = reverse_lazy('personal_list')

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super(RecipeCreate, self).form_valid(form)




class RecipeUpdate(LoginRequiredMixin, UpdateView):
    model = Recipe
    fields = ['title', 'description', 'video', 'image', 'number', 'ingredient', 'gram', 'cooking', 'category']
    success_url = reverse_lazy('personal_list')

class RecipeDelete(LoginRequiredMixin, DeleteView):
    model = Recipe
    success_url = reverse_lazy('personal_list')

    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)


