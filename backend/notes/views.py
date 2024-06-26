from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from notes.models import Note
# from rest_framework.views import APIView

from notes.serializers import NoteSerializer


# Create your views here.


class NoteBaseView:
    serializer_class = NoteSerializer
    permission_classes = (IsAuthenticated,)


class NoteCreate(CreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)            #FIXME


class NoteListCreate(ListAPIView):
    serializer_class = NoteSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)


class NoteUpdate(UpdateAPIView):
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)


class NoteDelete(DestroyAPIView):
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)


