from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FileCreate, FileList

app_name = 'api'

# upload/ - POST-запросы для загрузки файлов (ТОЛЬКО ПОСТ)
# files/ - список всех файлов с их данными, включая статус обработки.

urlpatterns = [
    path('upload/', FileCreate.as_view()),
    path('files/', FileList.as_view()),
]


# копипаста
# router = DefaultRouter()
# router.register('recipes', RecipeViewSet, basename='recipes')
# router.register('tags', TagViewSet, basename='tags')
# router.register('ingredients', IngredientViewSet, basename='ingredients')
# router.register('users', CustomUserViewSet)
#
# urlpatterns = [
#     path('', include(router.urls)),
#     path('', include('djoser.urls')),
#     path('auth/', include('djoser.urls.authtoken')),
# ]
