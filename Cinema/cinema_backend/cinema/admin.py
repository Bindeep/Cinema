from django.contrib import admin
from .models import Movie, Tag, Genre, UserProfile

admin.site.register([Movie, Tag, Genre, UserProfile])
