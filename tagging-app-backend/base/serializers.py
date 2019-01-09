from django.contrib.auth import get_user_model
from rest_framework import serializers

from . import models


class NoteNested(serializers.ModelSerializer):
    #tag_ids = serializers.PrimaryKeyRelatedField(source='tags', many=True, read_only=True)

    class Meta:
        model = models.Note

        fields = (
            'id',
            'name',

            #'tag_ids',
        )


class TagNested(serializers.ModelSerializer):
    parent_id = serializers.PrimaryKeyRelatedField(source='parent', read_only=True)

    #note_ids = serializers.PrimaryKeyRelatedField(source='notes', many=True, read_only=True)

    class Meta:
        model = models.Tag

        fields = (
            'id',
            'name',
            'type',
            'level',
            'lft',
            'rght',
            'tree_id',

            'parent_id',

            #'note_ids',
        )


class SynonymNested(serializers.ModelSerializer):
    master_id = serializers.PrimaryKeyRelatedField(source='master', read_only=True)

    class Meta:
        model = models.Synonym

        fields = (
            'id',
            'name',
            'type',

            'master_id',
        )


class Note(serializers.ModelSerializer):
    tags = TagNested(many=True, read_only=True)

    #tag_ids = serializers.PrimaryKeyRelatedField(
    #    source='tags',
    #    many=True,
    #    queryset=models.Tag.objects.all(),
    #    #write_only=True,
    #)

    class Meta:
        model = models.Note

        fields = (
            'id',
            'name',

            'tags',

            #'tag_ids',
        )


class Tag(serializers.ModelSerializer):
    parent = TagNested(read_only=True)

    #children = TagNested(many=True, read_only=True)

    descendant_ids = serializers.SerializerMethodField()

    synonyms = SynonymNested(many=True, read_only=True)

    #notes = NoteNested(many=True, read_only=True)

    note_ids = serializers.PrimaryKeyRelatedField(
        source='notes',
        many=True,
        queryset=models.Note.objects.all(),
        #write_only=True,
    )

    class Meta:
        model = models.Tag

        fields = (
            'id',
            'name',
            'type',
            'level',
            'lft',
            'rght',
            'tree_id',

            'parent',

            #'children',

            'descendant_ids',

            'synonyms',

            #'notes',
            'note_ids',
        )

    def get_descendant_ids(self, obj):
        return tuple(map(lambda x: x.id, obj.get_descendants()))


class Synonym(serializers.ModelSerializer):
    master = TagNested(read_only=True)

    class Meta:
        model = models.Synonym

        fields = (
            'id',
            'name',
            'type',

            'master',
        )


# import code; code.interact(local=dict(globals(), **locals()))
