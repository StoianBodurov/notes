from django.shortcuts import render, redirect

from notes.notes_app.forms import AddNoteForm, EditNoteForm, DetailsNoteForm, DeleteNoteForm
from notes.notes_app.models import Note
from notes.profiles.models import Profile


def home(request):
    profile = Profile.objects.first()
    if not profile:
        return redirect('creat profile')

    context = {
        'notes': Note.objects.all()

    }
    return render(request, 'home-with-profile.html', context)


def add_note(request):
    if request.method == 'POST':
        form = AddNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddNoteForm()
    context = {
        'form': form
    }
    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = EditNoteForm(instance=note)
    context = {
        'note': note,
        'form': form

    }
    return render(request, 'note-edit.html', context)


def details_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'note': note
        }
        return render(request, 'note-details.html', context)


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('home')
    else:
        form = DeleteNoteForm(instance=note)

    context = dict(note=note, form=form)

    return render(request, 'note-delete.html', context)
