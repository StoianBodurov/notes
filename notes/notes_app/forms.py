from django import forms

from notes.notes_app.models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'


class AddNoteForm(NoteForm):
    pass


class EditNoteForm(NoteForm):
    pass


class DeleteNoteForm(NoteForm):
    # pass
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'


class DetailsNoteForm(NoteForm):
    pass

