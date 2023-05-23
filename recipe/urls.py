from django.urls import path
from . import views

urlpatterns = [
    path('recipe/', views.RecipeView.as_view(), name='recipe_view'),
    path('recipe/<int:recipe_id>/', views.RecipeDetailView.as_view(), name='recipe_detail_view'),
    path('review/<int:recipe_id>/', views.ReviewView.as_view(), name='review_view'),
    path('review/detail/<int:review_id>/', views.ReviewDetailView.as_view(), name='review_detail_view'),
    path('review/comment/<int:pk>/', views.CommentView.as_view(), name='comment_view'),
    path('search/', views.SearchView.as_view(), name='search_view'),
]