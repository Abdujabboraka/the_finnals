from .models import FoodType, Food, Comment
from .serializer import FoodTypeSerializer, FoodSerializer, CommentSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import throttling

# Mixin views
class FoodTypeList(ModelViewSet):
    queryset = FoodType.objects.all()
    serializer_class = FoodTypeSerializer



# Model Viewset
class FoodViewSet(ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class CommentList(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

