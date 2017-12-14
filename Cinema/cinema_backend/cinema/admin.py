from django.contrib import admin
from django.contrib.auth.models import User
from .models import Movie, Tag, Genre, UserProfile

admin.site.register([Movie, Tag, Genre, UserProfile])