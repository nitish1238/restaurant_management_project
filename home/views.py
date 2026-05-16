from rest_framework.generics import ListAPIView
from .models import MenuCategory,MenuItem
from .serializers import MenuCategorySerializer, MenuItemSerializer
class MenuCategoryListView(ListAPIView):
    queryset=MenuCategory.objects.all()
    serializer_class=MenuCategorySerializer
class FeaturedMenuItem(ListAPIView):
    queryset=MenuItem.objects.filter(is_featured=True)
    serializer_class=MenuItemSerializer

