from django.contrib import admin

from .models.article import Article
from .models.category import Category


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    exclude = ("created_by", "modified_by")

    def save_model(self, request, obj, form, change):
        if not change and request.user.is_authenticated:
            obj.created_by = request.user

        elif change and request.user.is_authenticated:
            obj.modified_by = request.user

        super().save_model(request, obj, form, change)


admin.site.register(Category)
