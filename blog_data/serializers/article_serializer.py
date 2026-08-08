from rest_framework import serializers

from blog_data.models.article import Article


class ArticleSerializer(serializers.ModelSerializer):
    cover_image = serializers.ImageField(
        max_length=None, use_url=True,
    )

    class Meta:
        model = Article
        read_only_fields = fields = [
            'id',
            'title',
            'content',
            'excerpt',
            'created_by',
            'created_at',
            'updated_at',
            'is_published',
            'categories',
            'external_video_url',
            'cover_image',
            'image_gallery',
        ]

        # TODO: Think about readonly fields
