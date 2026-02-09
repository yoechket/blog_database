from django.contrib import admin

from .models.article import Article
from .models.category import Category

admin.site.register(Article)
admin.site.register(Category)
