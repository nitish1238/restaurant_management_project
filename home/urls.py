from django.urls import path
from .views import MenuCategoryListView,FeaturedMenuListView

urlpatterns = [
    path("menu-categories/",MenuCategoryListView.as_view(),name="menu-categories"),
    path("menu-items/featured/",FeaturedMenuListView.as_view(),name="featured-menu-items"),
    
]