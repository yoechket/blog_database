from django.contrib.auth import get_user_model
from django.db import models

from blog_data.TOOLS.AI.excerpt_gen import generate_excerpt_with_ollama

from .category import Category
from .gallery_image import GalleryImage

User = get_user_model()


class Article(models.Model):

    title = models.CharField(max_length=200)
    content = models.TextField(max_length=5000)
    excerpt = models.TextField(max_length=500, blank=True)

    categories = models.ManyToManyField(
        Category,
        blank=True,
        related_name='articles'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_visited = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='articles_created',
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='articles_modified'
    )
    external_video_url = models.URLField(max_length=500, null=True, blank=True)
    image_gallery = models.ManyToManyField(
            GalleryImage,
            blank=True,
            related_name='articles'
        )
    cover_image = models.ImageField(
        null=True,
        blank=True
    )
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Save first to get an ID for M2M

        if not self.excerpt:
            self.excerpt = generate_excerpt_with_ollama(
                self.title,
                self.content,
                self.categories.all()
            )
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']
