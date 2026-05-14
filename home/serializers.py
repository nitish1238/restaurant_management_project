from rest_framework import serializers
from .models import MenuCategory 
class MenuCategorySerializer(serializers.modelSerializer):
    class Meta:
        model=MenuCategory
        fields=['name']