from django.contrib import admin

from notes.notes_app.models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    pass