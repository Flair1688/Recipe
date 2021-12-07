from django.contrib.auth.views import LogoutView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('recipe/<int:pk>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('', views.RecipeList.as_view(), name='recipes'),
    path('personal_list/', views.PersonalAreaList.as_view(), name='personal_list'),
    path('filter/', views.FilterRecipeView.as_view(), name='filter'),
    path('search/', views.Search.as_view(), name='search'),

    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.RegisterPage.as_view(), name='register'),

    path('recipe-create/', views.RecipeCreate.as_view(), name='recipe-create'),
    path('recipe-update/<int:pk>/', views.RecipeUpdate.as_view(), name='recipe-update'),
    path('recipe-delete/<int:pk>/', views.RecipeDelete.as_view(), name='recipe-delete'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)