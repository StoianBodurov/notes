from django.urls import path

from notes.profiles.views import create_profile, profile_details, delete_profile

urlpatterns = [
    path('', profile_details, name='profile details'),
    path('create/', create_profile, name='creat profile'),
    path('delete/', delete_profile, name='delete profile'),
]