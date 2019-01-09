from django.contrib.auth import get_user_model
from rest_framework import serializers

from . import models


class NoteNested(serializers.ModelSerializer):
    #category_id = serializers.PrimaryKeyRelatedField(source='category', read_only=True)
    #_author_id = serializers.PrimaryKeyRelatedField(source='author', read_only=True)

    class Meta:
        model = models.Note

        fields = (
            'id',
            'name',
            #'category_id',
            #'_author_id',
        )


class CategoryNested(serializers.ModelSerializer):
    #note_ids = serializers.PrimaryKeyRelatedField(source='notes', many=True, read_only=True)

    class Meta:
        model = models.Category

        fields = (
            'id',
            'name',
            #'note_ids',
        )


class _AuthorNested(serializers.ModelSerializer):
    #note_ids = serializers.PrimaryKeyRelatedField(source='notes', many=True, read_only=True)

    class Meta:
        model = get_user_model()

        fields = (
            'id',
            'username',
            #'note_ids',
        )


class Note(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(
        source='category',
        queryset=models.Category.objects.all(),
        write_only=True,
    )

    category = CategoryNested(read_only=True)
    #_author = _AuthorNested(source='author', read_only=True)

    class Meta:
        model = models.Note

        fields = (
            'id',
            'name',
            'private',
            'share_count',
            'category_id',
            'category',
            #'_author',
        )


class Category(serializers.ModelSerializer):
    #notes = NoteNested(many=True, read_only=True)

    class Meta:
        model = models.Category

        fields = (
            'id',
            'name',
            #'notes',
        )
