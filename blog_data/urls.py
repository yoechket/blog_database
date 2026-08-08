from django.urls import path, include

from rest_framework.routers import DefaultRouter

from blog_data.views.article_view import ArticleViewSet


router = DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='article')

urlpatterns = [
    path('', include(router.urls)),
]
