from django.db import models
from django.urls import reverse
from slugify import unique_slugify
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Genre(models.Model):
	name = models.CharField(max_length = 30)

	def __str__(self):
		return self.name


class Movie(models.Model):
	name = models.CharField(max_length = 100, blank = False, null = False)
	genre = models.ForeignKey(Genre, related_name='genre', on_delete = models.DO_NOTHING)
	release_date = models.DateField(auto_now = False, auto_now_add = False)
	run_time = models.CharField(max_length = 15)
	cast = models.TextField()
	slug = models.SlugField(unique = True, blank = True, max_length = 50, null = True)
	poster = models.ImageField(upload_to = 'posters', null = True)


	def __str__(self):
		return self.name

	def save(self):
		self.slug = unique_slugify(self.name)
		super().save()

	def get_absolute_url(self):
		return reverse('movie:movie-list')


class Tag(models.Model):
	movie = models.ManyToManyField(Movie, related_name = 'movie')
	tag_name = models.CharField(max_length = 30)

	def  __str__(self):
		return self.tag_name
		

class UserProfile(models.Model):
	owner = models.OneToOneField(User, on_delete=models.CASCADE)
	phone_number = models.BigIntegerField(unique=True, default=0)
	gender = models.CharField(max_length=6, choices=(('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')))
	location = models.CharField(max_length=30)


	def __str__(self):
		return self.owner.username