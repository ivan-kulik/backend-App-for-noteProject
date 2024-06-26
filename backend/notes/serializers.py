from rest_framework.serializers import ModelSerializer

from notes.models import Note


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        # fields = ('pk', 'title', 'content', 'author')
        fields = ('pk', 'content', 'author', 'created_at')

    def create(self, validated_data):
        note = Note.objects.create(**validated_data)
        return note




