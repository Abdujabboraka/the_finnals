from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FoodTypeList, FoodViewSet ,CommentList

router = DefaultRouter()
router.register('foods', FoodViewSet)
router.register('food-types', FoodTypeList)
router.register('comments', CommentList)

urlpatterns = [
    path('', include(router.urls))
]