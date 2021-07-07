from django.shortcuts import render, redirect

from notes.notes_app.models import Note
from notes.profiles.forms import CreateProfileForm
from notes.profiles.models import Profile


def profile_details(request):
    profile = Profile.objects.first()
    notes_count = Note.objects.all().count()
    context = {
        'profile': profile,
        'notes_count': notes_count

    }
    return render(request, 'profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')


    context = {
        'form': CreateProfileForm()
    }
    return render(request, 'home-no-profile.html', context)


def delete_profile(request):
    profile = Profile.objects.first()
    notes = Note.objects.all()
    if request.method == 'GET':
        profile.delete()
        notes.delete()
        return redirect('home')
