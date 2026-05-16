from django.urls import path
from .views import MenuCategoryListView

urlpatterns = [
    path("menu-categories/",MenuCategoryListView.as_view(),name="menu-categories"),
    path("menu-items/featured/",FeaturedMenuListView.as_view(),name="featured-menu-items"),
    
]