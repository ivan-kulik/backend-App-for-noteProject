from django.urls import path
from . import views


urlpatterns = [
    path('', views.NoteListCreate.as_view(), name='all-notes'),
    path('create/', views.NoteCreate.as_view(), name='create-note'),
    path('update/', views.NoteUpdate.as_view(), name='update-note'),
    path('delete/<int:pk>/', views.NoteDelete.as_view(), name='delete-note'),
]

