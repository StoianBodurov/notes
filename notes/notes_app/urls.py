from django.urls import path

from notes.notes_app.views import home, add_note, edit_note, details_note, delete_note

urlpatterns = [
    path('', home, name='home'),
    path('add/', add_note, name='add_note'),
    path('edit/<int:pk>', edit_note, name='edit_note'),
    path('details/<int:pk>', details_note, name='details_note'),
    path('delite/<int:pk>', delete_note, name='delete_note'),
]
