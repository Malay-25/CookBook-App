from django.urls import path, include
from .views import home
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]