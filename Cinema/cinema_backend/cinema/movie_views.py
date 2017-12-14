from django.views.generic import ListView, DetailView, CreateView, UpdateView, View, DeleteView
from .models import Movie
from django.urls import reverse_lazy
from .forms import UserForm, ProfileForm
from django.shortcuts import render
import datetime


class MovieListView(ListView):
	today = datetime.date.today()
	ten_days_ago = today - datetime.timedelta(days = 10)
	model = Movie
	template_name = 'cinema/home.html'
	# context_object_name = 'Movies'

	def get_context_data(self, **kwargs):
	    context = super(MovieListView, self).get_context_data(**kwargs)
	    movies = Movie.objects.filter(release_date__gt = self.today)
	    now_showing = Movie.objects.filter(release_date__range = (self.ten_days_ago, self.today))
	    context = {
	    	'Movies' : movies,
	    	'now_showing_movies' : now_showing
	    }
	    return context


class MovieSearchView(View):
	template_name = 'cinema/home.html'

	def get(self, request):
		name = request.GET.get('name')
		movies = Movie.objects.filter(name__icontains=name)
		context = {

		'Movies' : movies
		}

		return render(request, 'cinema/home.html', context)


class MovieDetailView(DetailView):
	model = Movie
	template_name = 'cinema/detail.html'
	context_object_name = 'Movie'


class MovieCreateView(CreateView):
	model = Movie
	template_name = 'cinema/create.html'
	fields = ('name', 'genre', 'release_date', 'run_time', 'cast', 'poster')
	success_url = reverse_lazy('movie:movie-list')

	def get_context_data(self, **kwargs):
	    context = super(MovieCreateView, self).get_context_data(**kwargs)
	    context = {
	    	'Create' : 'Create',
	    	'form'   : self.get_form(),
	    	'Create_Movie' : 'Create New Movie',
	    	'Movie' : 'Movie'
	    }

	    return context

class MovieUpdateView(UpdateView):
	model = Movie
	template_name = 'cinema/create.html'
	fields = '__all__'
	success_url = reverse_lazy('movie:movie-list')

	def get_context_data(self, **kwargs):
	    context = super(MovieUpdateView, self).get_context_data(**kwargs)
	    
	    context = {
	    	'Update' : 'Update',
	    	'form'   : self.get_form(),
	    	'Update_Movie' : 'Update This Movie',
	    }

	    return context

class MovieDeleteView(DeleteView):
	model = Movie
	success_url = reverse_lazy('movie:movie-list')

	def get(self, request, *args, **kwargs):
		return self.post(request, *args, **kwargs)


